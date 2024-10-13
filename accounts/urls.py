from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path
from knox.views import LogoutView , LogoutAllView
router = DefaultRouter()

router.register(r'signup',  CreateUserAPI, basename='signup')
router.register(r'update_user',  UpdateUserAPI, basename='updateUser')

urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAllView.as_view(), name='logout')
    ]+ router.urls
