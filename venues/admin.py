from django.contrib import admin
from .models import Venues


# Register your models here.
@admin.register(Venues)
class VenuesAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "venue_type", "owner")
