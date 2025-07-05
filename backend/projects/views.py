#backend/projects/views.py

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from vacancy.models import Vacancy

from .models import Project
from .serializers import ProjectSerializer
from vacancy.serializers import VacancySerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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



