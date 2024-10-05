from django.db import models
from rest_framework import serializers
# Create your models here.

class Pokemon(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=300, unique=True)
    species = models.CharField(max_length=100)
    type = models.JSONField()