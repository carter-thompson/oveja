from enum import Enum
from django.db import models
from django.conf import settings

# Create your models here.
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

class LocationTypes(Enum):
    """
    Types of Locations
    """
    choices = (
        'unknown',
        'restaurant',
        'historical site',
        'religous',
        'theme park',
        'tourist attaction',
        'bar',
        'stadium',
        'beach',
        'museum',
        'park',
        'hotel',
        'hiking trail',
    )

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
        choices=LocationTypes.choices,
        default='unknown',
        null=False
    )
    order = models.IntegerField(null=False)
    address = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=2083, null=True)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Points of Interest"
