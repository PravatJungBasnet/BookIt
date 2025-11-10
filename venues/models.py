from django.db import models
from users.models import UserType
from datetime import timedelta


# Create your models here.
class VenuesType(models.TextChoices):
    FUTSAL = "FUTSAL", "Futsal"
    CRICKSAL = "CRICKSAL", "Cricksal"


class TimeSlotStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    UNAVAILABLE = "BOOKED", "Booked"


class Venues(models.Model):
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    venue_type = models.CharField(
        max_length=50, choices=VenuesType.choices, default=VenuesType.FUTSAL
    )
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    logo = models.ImageField(upload_to="venues", blank=True)
    cover_image = models.ImageField(upload_to="venues", blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    website_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    google_map_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    facilities = models.JSONField(default=list)

    @staticmethod
    def user_accessible_venues(user):
        if not user or not user.is_authenticated:
            return Venues.objects.all()

        if user.is_superuser or user.role == "ADMIN":
            return Venues.objects.all()
        if hasattr(user, "user_type") and user.user_type == UserType.PROVIDER:
            return Venues.objects.filter(owner=user)

        return Venues.objects.all()


class SlotConfigurationn(models.Model):
    venue = models.ForeignKey("venues.Venues", on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.DurationField(default=timedelta(minutes=60))
    # Pricing
    base_price_hour = models.FloatField()
    weekend_price_hour = models.FloatField(null=True, blank=True)


class TimeSlot(models.Model):
    venue = models.ForeignKey("venues.Venues", on_delete=models.CASCADE)
    slot_condiguartion = models.ForeignKey(
        "venues.SlotConfigurationn", on_delete=models.CASCADE
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.FloatField()
    status = models.CharField(
        max_length=50, choices=TimeSlotStatus.choices, default=TimeSlotStatus.AVAILABLE
    )
