from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project_Haslemere(models.Model):
    active = models.NullBooleanField(default=True)

    def __str__(self):
        name = "Project Haslemere"
        return self.name

class Project_Whiskey(models.Model):
    active = models.NullBooleanField(default=True)

class Data_Science(models.Model):
    active = models.NullBooleanField(default=True)
