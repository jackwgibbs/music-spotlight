from django.db import models


# Create your models here.

class Users(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=40)