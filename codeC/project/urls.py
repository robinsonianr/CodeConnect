from django.urls import path
from .views import CreateProject


urlpatterns = [
    path('create/', CreateProject.as_view(), name='project_create'), 
]