from django.urls import path
from userProfile.views import ProfileDetails, CreateUserProfile


urlpatterns = [
    path('profile/<str:pk>', ProfileDetails.as_view(), name='profile_details'),
    path('register/', CreateUserProfile.as_view(), name='register_profile')
]