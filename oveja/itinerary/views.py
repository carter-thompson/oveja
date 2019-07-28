from rest_framework import generics
from .models import Itinerary
from .serializers import ItinerarySerializer

class ListItineraryView(generics.ListAPIView):
    """
    Provide GET method handler
    """
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
