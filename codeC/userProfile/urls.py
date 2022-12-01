from django.urls import path
from userProfile.views import ProfileDetails, CreateUserProfile, EditProfile


urlpatterns = [
    path('profile/<str:pk>', ProfileDetails.as_view(), name='profile_details'),
    path('edit/<str:pk>', EditProfile.as_view(), name='edit_profile'),
    path('register/', CreateUserProfile.as_view(), name='register_profile')
]