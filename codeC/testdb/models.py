from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField(max_length=50)

    brand = models.CharField(max_length=50)

    price = models.IntegerField()