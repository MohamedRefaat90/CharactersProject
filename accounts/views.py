from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# from knox import views as knox_views
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
# Create your views here.

class CreateUserAPI (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class UpdateUserAPI (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (AllowAny,)
    
# class LoginAPI(knox_views.LoginView):
#     # queryset = User.objects
#     # serializer_class = LoginSerializer
#     permission_classes = () 
    
#     def post(self, request, format= None):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data['user']
#             authenticate(username=user.email, password=user.password)
#         login(request, user)
    
#         return super(LoginAPI, self).post(request, format=None)

    
        