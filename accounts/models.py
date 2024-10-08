from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class user(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False, unique= True)
    password = models.CharField(max_length=128, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # This is the field that is used to log in
    USERNAME_FIELD = 'email'