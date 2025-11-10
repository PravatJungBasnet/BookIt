from django.contrib import admin
from .models import Venues, SlotConfigurationn, TimeSlot


# Register your models here.
@admin.register(Venues)
class VenuesAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "venue_type", "owner")


@admin.register(SlotConfigurationn)
class SlotConfigurationnAdmin(admin.ModelAdmin):
    list_display = (
        "venue",
        "start_time",
        "end_time",
        "duration",
        "base_price_hour",
        "weekend_price_hour",
    )


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        "venue",
        "slot_condiguartion",
        "date",
        "start_time",
        "end_time",
        "price",
        "status",
    )
