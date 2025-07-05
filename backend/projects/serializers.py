# backend/projects/serializers.py

from datetime import date
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(
        read_only=True,
        help_text="Unique identifier of the project."
    )
    title = serializers.CharField(
        required=True,
        max_length=100,
        help_text="Project title. Required field."
    )
    description = serializers.CharField(
        required=False,
        help_text="Detailed description of the project."
    )
    deadline = serializers.DateField(
        required=True,
        help_text="Deadline in YYYY-MM-DD format. Cannot be in the past."
    )
    created_at = serializers.DateTimeField(
        read_only=True,
        help_text="Timestamp when the project was created."
    )
    updated_at = serializers.DateTimeField(
        read_only=True,
        help_text="Timestamp when the project was last updated."
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "deadline",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def to_internal_value(self, data):

        extra = set(data.keys()) - set(self.fields.keys())
        if extra:
            raise serializers.ValidationError(
                {field: "Unexpected field." for field in extra}
            )

        return super().to_internal_value(data)

    def validate(self, attrs):
        errors = {}


        for field in ("title", "deadline"):
            if field not in attrs:
                errors[field] = ["This field is required."]


        if "deadline" in attrs and attrs["deadline"] < date.today():
            errors["deadline"] = ["Deadline cannot be in the past."]

        if errors:
            raise serializers.ValidationError(errors)

        return attrs
