from email.policy import default
from django.db import models
import uuid

# Create your models here.

def uuid_generator():
    return uuid.uuid4().hex

class Profile(models.Model):
    uid = models.TextField(primary_key=True,
     default=uuid_generator, editable=False)

    email = models.EmailField(max_length=254, default=None)
     
    username = models.CharField(max_length=20, blank=True, null=True)

    bio = models.TextField(max_length=255,blank=True, null=True)

    skills = models.CharField(max_length=128, blank=True, null=True)

    pfp = models.ImageField(upload_to='profile_pics', default='profile_pics/default.png')