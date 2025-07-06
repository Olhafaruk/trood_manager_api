#vacancy/models.py

from django.db import models
from projects.models import Project
from datetime import date

class Vacancy(models.Model):
    project = models.ForeignKey(Project, related_name='vacancies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(default=date.today)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.project.title})"
