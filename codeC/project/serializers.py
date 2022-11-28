from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('pid', 'title', 'description', 'users', 'languages', 'beg_friendly')