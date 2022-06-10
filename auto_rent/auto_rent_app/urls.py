from rest_framework import routers
from .views import CarsViewSet
router = routers.DefaultRouter()
router.register('api/auto_rent', CarsViewSet, 'cars')

urlpatterns = router.urls
