from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snowflake_app import views 

router = DefaultRouter()
router.register("trips", views.TripViews, basename="trip")
router.register("trips-limited", views.TripLimitedViewSet, basename="trip-limited")

urlpatterns = [
    path('view/', include(router.urls)),
    path('view/trips/date/<str:trip_date>/', views.TripViews.as_view({'get': 'get_by_date'}), name='trip-by-date'),
]
