from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VenueViewSet, SlotConfigurationViewSet, TimeSlotView

app_name = "venues"
router = DefaultRouter()
router.register("", VenueViewSet, basename="venues")
router.register(
    r"(?P<venue_id>\d+)/slotconfig", SlotConfigurationViewSet, basename="slotconfig"
)
router.register(r"(?P<venue_id>\d+)/timeslots", TimeSlotView, basename="timeslots")

urlpatterns = [path("", include(router.urls))]
