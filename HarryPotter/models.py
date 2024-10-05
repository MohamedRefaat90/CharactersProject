from django.db import models

# Create your models here.

class HarryPotterCharacter(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=10)
    house = models.CharField(max_length=50)
    yearOfBirth = models.CharField(max_length=10)
    ancestry = models.CharField(max_length=50)
    patronus = models.CharField(max_length=50)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name