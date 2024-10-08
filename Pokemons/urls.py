from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',  PokemonViewset, basename='Pokemons')

urlpatterns = router.urls  