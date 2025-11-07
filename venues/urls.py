from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VenueViewSet

app_name = "venues"
router = DefaultRouter()
router.register("", VenueViewSet, basename="venues")
urlpatterns = [path("", include(router.urls))]
