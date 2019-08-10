"""
Itinerary Views
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .models import Itinerary
from .serializers import ItinerarySerializer

class ListItinerariesView(generics.ListCreateAPIView):
    """
    Provide GET method handler for all Itinerary objects
    """
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer

class ItineraryDetail(APIView):
    """
    Retrieve Itinerary
    """
    def get_itinerary(self, pk):
        """
        get Itinerary by PK
        """
        try:
            return Itinerary.objects.get(pk=pk)
        except Itinerary.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        GET single Itinerary
        """
        itinerary = self.get_itinerary(pk)
        serializer = ItinerarySerializer(itinerary)
        return Response(serializer.data)
