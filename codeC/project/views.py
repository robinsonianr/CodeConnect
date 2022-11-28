from requests import request
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics

# Create your views here.


class CreateProject(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data

        
        django_project, _ = Project.objects.get_or_create(title=data['title'], description=data['description'], users=data['users'], 
        languages=data['languages'])
        django_project.save()

        return Response(data, status=status.HTTP_201_CREATED)



class ProjectDetails(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()