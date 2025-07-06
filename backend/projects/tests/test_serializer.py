# backend/projects/tests/test_serializer.py

from datetime import date, timedelta
from django.test import TestCase
from projects.serializers import ProjectSerializer


class TestProjectSerializer(TestCase):
    def test_valid_data(self):
        data = {
            "title": "Website Redesign",
            "deadline": str(date.today() + timedelta(days=5)),
        }
        serializer = ProjectSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_missing_title(self):
        data = {
            "deadline": str(date.today() + timedelta(days=5)),
        }
        serializer = ProjectSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_deadline_in_past(self):
        data = {
            "title": "Legacy",
            "deadline": str(date.today() - timedelta(days=1)),
        }
        serializer = ProjectSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("deadline", serializer.errors)

    def test_extra_field_rejected(self):
        data = {
            "title": "X",
            "deadline": str(date.today() + timedelta(days=5)),
            "foo": "bar",
        }
        serializer = ProjectSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("foo", serializer.errors)
