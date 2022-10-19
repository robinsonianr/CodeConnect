import firebase_admin
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import credentials
from firebase_admin import auth
from rest_framework import authentication

from .exceptions import FirebaseError, NoAuthToken, InvalidAuthToken

cred = credentials.Certificate("C:/Users/ianrr/FirebaseAuth/codeconnect-450a4-firebase-adminsdk-frmzw-872744fbf8.json")
app = firebase_admin.initialize_app(cred)


class FirebaseAuthenication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return (user, None)