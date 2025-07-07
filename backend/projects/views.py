#backend/projects/views.py

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from vacancy.models import Vacancy

from .models import Project
from .serializers import ProjectSerializer
from vacancy.serializers import VacancySerializer

from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Projects"])
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(detail=True, methods=["get", "post"])
    def vacancies(self, request, pk=None):
        project = self.get_object()

        if request.method == "GET":
            vacancies = project.vacancies.all()
            serializer = VacancySerializer(vacancies, many=True)
            return Response(serializer.data)

        if request.method == "POST":
            data = request.data.copy()
            data["project"] = project.id
            serializer = VacancySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(summary="List all projects", tags=["Projects"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Create a project", tags=["Projects"])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Retrieve project by ID", tags=["Projects"])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Update project", tags=["Projects"])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Delete project", tags=["Projects"])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



