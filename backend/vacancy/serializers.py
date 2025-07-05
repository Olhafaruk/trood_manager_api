#backend/vacancy/serializers.py

from rest_framework import serializers
from .models import Vacancy
from projects.models import Project
from datetime import date

class VacancySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True,
        help_text="Unique identifier of the vacancy."
    )
    title = serializers.CharField(
        max_length=100,
        help_text="Job title or position name.",

    )
    description = serializers.CharField(
        required=False,
        help_text="Detailed description of the vacancy."
    )
    salary = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Offered salary in USD. Must be non-negative."
    )
    deadline = serializers.DateField(
        help_text="Application deadline in YYYY-MM-DD format. Cannot be in the past."
    )
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        help_text="ID of the related project."
    )
    created_at = serializers.DateTimeField(
        read_only=True,
        help_text="Timestamp when the vacancy was created."
    )
    updated_at = serializers.DateTimeField(
        read_only=True,
        help_text="Timestamp when the vacancy was last updated."
    )

    class Meta:
        model = Vacancy
        fields = (
            "id",
            "title",
            "description",
            "salary",
            "deadline",
            "project",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_deadline(self, value):
        if value < date.today():
            raise serializers.ValidationError("Deadline cannot be in the past.")
        return value

    def validate_salary(self, value):

        if value <= 0:
            raise serializers.ValidationError("Salary must be greater than zero.")
        return value

    def to_internal_value(self, data):

        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "Unexpected field."})
        return super().to_internal_value(data)
