from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'',  HarryPotterViewset, basename='HarryPotter')

urlpatterns = router.urls
