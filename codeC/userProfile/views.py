from requests import request
from .models import Profile
import pyrebase
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

firebaseConfig = {
  "apiKey": "AIzaSyBGmQMfE3AyEocDnQ3_K0eXuL3wZmaHiHU",
  "authDomain": "codeconnect-450a4.firebaseapp.com",
  "projectId": "codeconnect-450a4",
  "databaseURL": "https://codeconnect-450a4-default-rtdb.firebaseio.com",
  "storageBucket": "codeconnect-450a4.appspot.com",
  "messagingSenderId": "208324474214",
  "appId": "1:208324474214:web:b89099c836fad398ff84a7",
  "measurementId": "G-EM44RHS228"
};

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Create your views here.

class CreateUserProfile(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data

        try:
          user = auth.create_user_with_email_and_password(data['email'], data["password"])
          auth.send_email_verification(user['idToken'])
          
          print("email verification sent")
          
          django_user, _ = Profile.objects.get_or_create(uid=user["localId"], email=user['email'])
          django_user.save()
          return Response(user, status=status.HTTP_201_CREATED)
        except:
          print("Email Already Exist")
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
