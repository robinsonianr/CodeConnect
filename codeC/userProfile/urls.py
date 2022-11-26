from django.urls import path
from userProfile.views import ProfileDetails


urlpatterns = [
    path('profile/<str:pk>', ProfileDetails.as_view(), name='profile_details'),
]