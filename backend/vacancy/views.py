#backend/vacancy/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema
from .models import Vacancy
from .serializers import VacancySerializer



@extend_schema(tags=["Vacancies"])
class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('-created_at')
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        qs = super().get_queryset()
        return qs.filter(project_id=project_id) if project_id else qs

    @extend_schema(summary="List all vacancies", tags=["Vacancies"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Create a vacancy", tags=["Vacancies"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Retrieve vacancy by ID", tags=["Vacancies"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Update vacancy", tags=["Vacancies"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Delete vacancy", tags=["Vacancies"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




