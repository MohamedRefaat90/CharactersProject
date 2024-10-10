from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path
router = DefaultRouter()

router.register(r'create_user',  CreateUserAPI, basename='createUser')
router.register(r'update_user',  UpdateUserAPI, basename='updateUser')

urlpatterns = [
    # path('login/', LoginAPI.as_view(), name='login')
    ]+ router.urls
