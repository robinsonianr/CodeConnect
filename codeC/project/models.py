from django.db import models
import uuid

def uuid_generator():
    return uuid.uuid4().hex

class Project(models.Model):

    pid = models.TextField(primary_key=True,
    default=uuid_generator, editable=False)

    title = models.CharField(max_length=64, default=None)

    description = models.CharField(max_length=255)
     
    users = models.JSONField()

    languages = models.JSONField()

    beg_friendly = models.BooleanField(default=False)
