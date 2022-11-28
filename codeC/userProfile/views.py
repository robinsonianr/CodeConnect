from requests import request

from userProfile.serializers import UserProfileSerializer
from .models import Profile
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, generics

# Create your views here.

class CreateUserProfile(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data

        try:
          django_user, _ = Profile.objects.get_or_create(uid=data["localID"], email=data['email'], username=data['username'], displayName=data['username'])
          django_user.save()
          return Response(data, status=status.HTTP_201_CREATED)
        except:
          print("Email already exist or error connecting to local database.")
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        


class ProfileDetails(generics.RetrieveAPIView):
  permission_classes = [AllowAny]
  serializer_class = UserProfileSerializer
  queryset = Profile.objects.all()



class EditProfile(generics.UpdateAPIView):
  permission_classes = [AllowAny]
  serializer_class = UserProfileSerializer
  queryset = Profile.objects.all