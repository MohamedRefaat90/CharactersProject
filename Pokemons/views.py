from django.shortcuts import render
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer
from common.pagination import CustomPagination
# Create your views here.

class PokemonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    pagination_class = CustomPagination
