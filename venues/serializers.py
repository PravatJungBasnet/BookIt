from .models import Venues
from rest_framework.serializers import ModelSerializer


class VenueSerializer(ModelSerializer):
    class Meta:
        model = Venues
        fields = [
            "id",
            "name",
            "location",
            "venue_type",
            "description",
            "opening_time",
            "closing_time",
            "logo",
            "cover_image",
            "website_url",
            "facebook_url",
            "instagram_url",
            "google_map_url",
            "is_available",
            "facilities",
            "created_at",
            "updated_at",
        ]
