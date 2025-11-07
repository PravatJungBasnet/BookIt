from .models import Venues

from .serializers import VenueSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsownerOrReadOnly


# Create your views here.
class VenueViewSet(ModelViewSet):
    queryset = Venues.objects.all()
    serializer_class = VenueSerializer
    permission_classes = [IsownerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Venues.user_accessible_venues(self.request.user)
