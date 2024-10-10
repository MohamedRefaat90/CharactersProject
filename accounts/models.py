from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


# UserManager: A manager class that defines how CustomUser instances (users)
# are created, either as regular users or superusers.
# It doesn't represent a user but provides functionality to handle user creation.
class UserManager(BaseUserManager):

        def create_user(self, email, password, **extra_fields):
            if not email:
                raise ValueError("The email is not given.")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.is_active = True
            user.set_password(password)
            user.save()
            return user
        
        def create_superuser(self, email, password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)
            
            if not extra_fields.get('is_staff'):
                raise ValueError('Superuser must have is_staff=True')
            if not extra_fields.get('is_superuser'):
                raise ValueError('Superuser must have is_superuser=True')
            
            return self.create_user(email, password, **extra_fields)


# User: The model that represents an individual user in the system,
# containing fields like email, name, and status (is_staff, is_superuser),
# and is managed by UserManager
class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False, unique= True)
    password = models.CharField(max_length=128, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # This is the field that is used to log in
    USERNAME_FIELD = 'email'

    objects = UserManager()
    
    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True