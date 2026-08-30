from django.db import models


class LocationStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    BLOCKED = "BLOCKED", "Blocked"
    QUARANTINE = "QUARANTINE", "Quarantine"


class UnitOfMeasure(models.TextChoices):
    PALLET = "PL", "Pallet"
    KILOGRAM = "KG", "Kilogram"
    LITER = "L", "Liter"
    METER = "M", "Meter"


class LocationType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Plant(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Storage(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.PROTECT,related_name="storages")
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    name = models.CharField(max_length=20, unique=True)
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT, related_name= "locations")
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    capacity_unit = models.CharField(max_length=2,choices=UnitOfMeasure.choices)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT, related_name="locations")
    status = models.CharField(max_length=20,choices=LocationStatus.choices, default=LocationStatus.AVAILABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
