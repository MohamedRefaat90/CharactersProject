from rest_framework import serializers
from .models import HarryPotterCharacter

class HarryPotterCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarryPotterCharacter
        fields = '__all__'