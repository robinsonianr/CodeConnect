from requests import request
from .models import Profile
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CreateProject(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data

        
        django_project, _ = Profile.objects.get_or_create(title=data['title'], description=data['description'], users=data['users'], 
        languages=data['languages'], beg_friendly=data['beg_friendly'])
        django_project.save()

        return Response(data, status=status.HTTP_201_CREATED)

        
        
