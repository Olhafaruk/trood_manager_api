#backend/projects/tests/test_api.py

from datetime import date, timedelta
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from projects.models import Project
from vacancy.models import Vacancy

class TestProjectAPI(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="olha", password="1234")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('project-list')
        self.payload = {
            "title": "API Project",
            "description": "Integration test",
            "deadline": str(date.today() + timedelta(days=7)),
        }

    def test_list_empty(self):
        resp = self.client.get(self.list_url, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, [])

    def test_create_success(self):
        resp = self.client.post(self.list_url, self.payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', resp.data)
        self.assertEqual(resp.data['title'], self.payload['title'])

    def test_create_missing_title(self):
        data = {"deadline": self.payload["deadline"]}
        resp = self.client.post(self.list_url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', resp.data)

    def test_retrieve_update_delete(self):
        proj = Project.objects.create(
            title="Old", deadline=date.today() + timedelta(days=5)
        )
        detail = reverse('project-detail', args=[proj.id])

        # retrieve
        r = self.client.get(detail, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['id'], proj.id)

        # update
        new_deadline = str(date.today() + timedelta(days=10))
        r = self.client.patch(detail, {"title": "New", "deadline": new_deadline}, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['title'], "New")

        # delete
        r = self.client.delete(detail)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=proj.id).exists())

class TestProjectVacanciesNestedAPI(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="nested_user", password="1234")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.project = Project.objects.create(
            title="Nested", deadline=date.today() + timedelta(days=30)
        )
        self.nested_url = reverse('project-vacancies', args=[self.project.id])
        self.existing = Vacancy.objects.create(
            project=self.project,
            title="Exist",
            description="Desc",
            salary="1000.00",
            deadline=date.today() + timedelta(days=5)
        )

    def test_list_nested(self):
        r = self.client.get(self.nested_url, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        ids = [v['id'] for v in r.data]
        self.assertIn(self.existing.id, ids)

    def test_create_nested_success(self):
        data = {
            "title": "New Vac",
            "description": "Nested test",
            "salary": "1200.00",
            "deadline": str(date.today() + timedelta(days=3)),
        }
        r = self.client.post(self.nested_url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data['project'], self.project.id)

    def test_create_nested_bad_deadline(self):
        data = {
            "title": "Bad",
            "description": "Desc",
            "salary": "1100.00",
            "deadline": str(date.today() - timedelta(days=1)),
        }
        r = self.client.post(self.nested_url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('deadline', r.data)
