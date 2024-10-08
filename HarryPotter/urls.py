from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'',  HarryPotterViewset, basename='HarryPotter')
# router.register(r'<str: character_id>',  CharacterByIDViewset, basename='CharacterByID')

urlpatterns = router.urls
