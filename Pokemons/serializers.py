from rest_framework import serializers
from .models import Pokemon

# Create your models here.

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'