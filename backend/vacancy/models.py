#vacancy/models.py

from django.db import models
from projects.models import Project

class Vacancy(models.Model):
    project = models.ForeignKey(Project, related_name='vacancies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.project.title})"

