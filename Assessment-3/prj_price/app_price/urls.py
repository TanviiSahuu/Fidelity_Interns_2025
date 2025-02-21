from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PriceViewSet, PriceLocationCustom

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'prices', PriceViewSet, basename='price')
router.register(r'prices-location', PriceLocationCustom, basename='price-location')

urlpatterns = [
    path('items/', include(router.urls)),
    path('priceslocation/', PriceLocationCustom.as_view({'get': 'get_both'}), name='get-both-prices-locations'),
]
