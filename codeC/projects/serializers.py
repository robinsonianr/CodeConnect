import imp
from rest_framework import serializers
from .models import Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pid', 'title', 'description', 'users', 'languages', 'beg_friendly')