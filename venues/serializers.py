from .models import Venues, SlotConfigurationn, TimeSlot, Sport
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


class SportSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = ["id", "name", "icon"]


class SlotConfigurationSerializer(ModelSerializer):
    class Meta:
        model = SlotConfigurationn
        fields = [
            "id",
            "venue",
            "sport",
            "start_time",
            "end_time",
            "duration",
            "base_price_hour",
            "weekend_price_hour",
        ]


class TimeSlotSerializer(ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = [
            "id",
            "venue",
            "slot_condiguartion",
            "date",
            "start_time",
            "end_time",
            "price",
            "status",
        ]
