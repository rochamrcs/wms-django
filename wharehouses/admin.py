from django.contrib import admin
from .models import LocationType, Plant, Storage, Location


admin.site.register(LocationType)
admin.site.register(Plant)
admin.site.register(Storage)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["address", "storage", "capacity", "capacity_unit", "location_type", "status"]
