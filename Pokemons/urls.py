from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',  PokemonViewset, basename='Pokemons')
router.register(r'<int: pokemon_id>',  PokemonByIDViewset, basename='PokemonByID')


urlpatterns = router.urls  