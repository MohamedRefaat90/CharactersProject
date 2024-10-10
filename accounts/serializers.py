from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name')


class CreateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists')
        
        return attrs
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class UpdateUserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=False)
    email = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password')
        
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email').lower().strip()
        password = attrs.get('password')

        if email and password:
            # Authenticate the user
            user = authenticate(username=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")
        
        attrs['user'] = user
        return attrs
