#backend/vacancy/tests/test_api

from datetime import date, timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from projects.models import Project
from vacancy.models import Vacancy

class TestVacancyAPI(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="FilterProj", deadline=date.today() + timedelta(days=20)
        )
        self.list_url = reverse('vacancy-list')
        self.valid = {
            "title": "API Dev",
            "description": "Integration",
            "salary": "2000.00",
            "deadline": str(date.today() + timedelta(days=7)),
            "project": self.project.id,
        }

    def test_list_empty(self):
        r = self.client.get(self.list_url, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data, [])

    def test_filter_by_project(self):
        v1 = Vacancy.objects.create(
            project=self.project,
            title="V1", description="D1",
            salary="1500.00",
            deadline=date.today() + timedelta(days=5)
        )
        other = Project.objects.create(
            title="Other", deadline=date.today() + timedelta(days=5)
        )
        Vacancy.objects.create(
            project=other,
            title="V2", description="D2",
            salary="1600.00",
            deadline=date.today() + timedelta(days=3)
        )

        r = self.client.get(self.list_url + f"?project={self.project.id}", format='json')
        ids = [v['id'] for v in r.data]
        self.assertIn(v1.id, ids)
        self.assertFalse(any(v['id'] != v1.id for v in r.data))

    def test_create_success_and_retrieve(self):
        r = self.client.post(self.list_url, self.valid, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        vac_id = r.data['id']

        detail = reverse('vacancy-detail', args=[vac_id])
        r = self.client.get(detail, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['id'], vac_id)

    def test_update_and_delete(self):
        vac = Vacancy.objects.create(**self.valid)
        detail = reverse('vacancy-detail', args=[vac.id])

        # update
        r = self.client.patch(detail, {"title": "Upd"}, format='json')
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['title'], "Upd")

        # delete
        r = self.client.delete(detail)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vacancy.objects.filter(id=vac.id).exists())

    def test_create_invalid_salary(self):
        bad = self.valid.copy()
        bad['salary'] = "-500.00"
        r = self.client.post(self.list_url, bad, format='json')
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('salary', r.data)
