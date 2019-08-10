"""
Itinerary Serializers
"""

from rest_framework import serializers
from .models import Itinerary, POI

class POISerializer(serializers.ModelSerializer):
    """
    Point of Interest Serializer
    """
    class Meta:
        model = POI
        fields = (
            "name",
            "itinerary",
            "latitude",
            "longitude",
            "location_type",
            "order",
            "address",
            "image",
            "website",
            )

class ItinerarySerializer(serializers.ModelSerializer):
    """
    Itinerary Serializer
    """
    class Meta:
        model = Itinerary
        points_of_interest = POISerializer(many=True, read_only=True)
        fields = ("title", "owner", "is_published")
