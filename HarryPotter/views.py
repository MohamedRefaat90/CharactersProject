from django.shortcuts import render
from rest_framework import viewsets
from .models import HarryPotterCharacter
from .serializer  import HarryPotterCharacterSerializer

# Create your views here.

class HarryPotterViewset(viewsets.ReadOnlyModelViewSet):
    queryset = HarryPotterCharacter.objects.all()
    serializer_class = HarryPotterCharacterSerializer