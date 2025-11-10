from .models import Venues, SlotConfigurationn, TimeSlot
from django.shortcuts import get_object_or_404
from .serializers import (
    VenueSerializer,
    SlotConfigurationSerializer,
    TimeSlotSerializer,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from .permissions import IsownerOrReadOnly
from rest_framework.permissions import AllowAny


# Create your views here.
class VenueViewSet(ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsownerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Venues.user_accessible_venues(self.request.user)


class SlotConfigurationViewSet(ModelViewSet):
    serializer_class = SlotConfigurationSerializer

    def get_queryset(self):
        venue_id = self.kwargs.get("venue_id")
        return SlotConfigurationn.objects.filter(venue_id=venue_id)

    def perform_create(self, serializer):
        venue_id = self.kwargs.get("venue_id")
        venue = get_object_or_404(Venues, id=venue_id)
        serializer.save(venue=venue)


class TimeSlotView(ReadOnlyModelViewSet):
    serializer_class = TimeSlotSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        venue_id = self.kwargs.get("venue_id")
        return TimeSlot.objects.filter(venue_id=venue_id)
