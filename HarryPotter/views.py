from django.shortcuts import render
from rest_framework import viewsets
from .models import HarryPotterCharacter
from .serializer  import HarryPotterCharacterSerializer
from common.pagination import CustomPagination


# Create your views here.

class HarryPotterViewset(viewsets.ReadOnlyModelViewSet):
    queryset = HarryPotterCharacter.objects.all()
    serializer_class = HarryPotterCharacterSerializer
    pagination_class = CustomPagination
