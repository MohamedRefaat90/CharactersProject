from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from knox import views as knox_views
from django.contrib.auth import login
from rest_framework import  permissions,viewsets
from drf_spectacular.utils import extend_schema, OpenApiExample


# Create your views here.

class CreateUserAPI (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class UpdateUserAPI (viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (AllowAny,)
    
class LoginAPI(knox_views.LoginView):
    permission_classes = (permissions.AllowAny,)
    
    @extend_schema(
        summary="User Login",
        description="Authenticate a user and retrieve an auth token.",
        request=LoginSerializer,
        responses={
            200: OpenApiExample(
                "Success",
                description="Returns user data and auth token",
                value={
                    "user": {"username": "testuser"},
                    "token": "sample-token-123456"
                }
            ),
            400: OpenApiExample(
                "Invalid Credentials",
                description="Invalid username or password",
                value={"detail": "Invalid credentials"}
            )
        },
    )

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        
        # Validate serializer and check credentials
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Log the user in
        login(request, user)

        # Generate token using Knox's parent class method
        response = super(LoginAPI, self).post(request, format=None)

        # Return success response with user data and token
        return Response({
            'user': UserSerializer(user).data,
            'token': response.data['token']
        }, status=status.HTTP_200_OK)

    
        