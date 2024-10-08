from django.db import models

# Create your models here.

class HarryPotterCharacter(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=10, null=True)
    house = models.CharField(max_length=50, null=True)
    yearOfBirth = models.CharField(max_length=10, null=True)
    ancestry = models.CharField(max_length=50, null=True)
    patronus = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name