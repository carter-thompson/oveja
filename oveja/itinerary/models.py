"""
Itinerary Models
"""
from django.db import models
from django.conf import settings

from .choices import Locations

class Itinerary(models.Model):
    """
    Itinerary Model
    """
    title = models.CharField(max_length=255, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.owner)

    class Meta:
        verbose_name_plural = "Itineraries"

class POI(models.Model):
    """
    Point Of Interest in an Itinerary
    """
    name = models.CharField(max_length=255, null=False)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    location_type = models.CharField(
        max_length=255,
        choices=Locations.CHOICES,
        default=Locations.OTHER,
        null=False
    )
    order = models.IntegerField(null=False)
    address = models.CharField(max_length=255, null=True, blank=False)
    image = models.CharField(max_length=255, null=True, blank=False)
    website = models.CharField(max_length=2083, null=True, blank=False)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Points of Interest"
