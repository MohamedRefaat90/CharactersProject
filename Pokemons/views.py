from django.shortcuts import render
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer

# Create your views here.

class PokemonViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonByIDViewset(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer

    def get_queryset(self, pokemon_id):
        return Pokemon.objects.filter(pk = pokemon_id)