from rest_framework import serializers
from .models import Itinerary

class ItinerarySerializer(serializers.ModelSerializer):
    """
    Itinerary Serializer
    """
    class Meta:
        model = Itinerary
        fields = ("title", "owner", "is_published")
        