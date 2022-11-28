import imp
from rest_framework import serializers
from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('uid', 'email', 'username', 'displayName', 'bio', 'skills', 'pfp', 'spotlightProj', 'pinned')