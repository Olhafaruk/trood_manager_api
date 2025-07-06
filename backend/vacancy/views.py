#backend/vacancy/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('-created_at')
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        qs = super().get_queryset()
        return qs.filter(project_id=project_id) if project_id else qs




