# backend/vacancy/tests/test_serializer.py

from datetime import date, timedelta
from django.test import TestCase
from projects.models import Project
from vacancy.serializers import VacancySerializer


class TestVacancySerializer(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
        title="Alpha",
        deadline=date.today() + timedelta(days=30)
        )

    def test_valid_data(self):

        data = {
            "title": "Backend Developer",
            "description": "Work on API endpoints",
            "salary": "3000.00",
            "deadline": str(date.today() + timedelta(days=7)),
            "project": self.project.id,
        }
        serializer = VacancySerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_missing_title(self):

        data = {
            "salary": "1000.00",
            "deadline": str(date.today() + timedelta(days=7)),
            "project": self.project.id,
        }
        serializer = VacancySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_negative_salary(self):

        data = {
            "title": "QA Engineer",
            "salary": "-100.00",
            "deadline": str(date.today() + timedelta(days=7)),
            "project": self.project.id,
        }
        serializer = VacancySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("salary", serializer.errors)

    def test_deadline_in_past(self):

        data = {
            "title": "DevOps Engineer",
            "salary": "2500.00",
            "deadline": str(date.today() - timedelta(days=1)),
            "project": self.project.id,
        }
        serializer = VacancySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("deadline", serializer.errors)

    def test_invalid_project(self):

        data = {
            "title": "Frontend Dev",
            "salary": "2000.00",
            "deadline": str(date.today() + timedelta(days=5)),
            "project": 9999,  # такого ID нет
        }
        serializer = VacancySerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("project", serializer.errors)

