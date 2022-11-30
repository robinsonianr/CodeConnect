from django.urls import path
from .views import CreateProject, ProjectDetails


urlpatterns = [
    path('create/', CreateProject.as_view(), name='project_create'), 
    path('view/', ProjectDetails.as_view(), name='view all projects')
]