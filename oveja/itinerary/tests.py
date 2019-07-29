from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Itinerary
from .serializers import ItinerarySerializer, POISerializer


class BaseViewTest(APITestCase):
    """
    Base View Test
    """
    client = APIClient()

    @staticmethod
    def create_itinerary(title, owner, is_published):
        """
        Create itinerary object
        """
        Itinerary.objects.create(title=title, owner=owner, is_published=is_published)

    def setUp(self):
        """
        Setup
        """
        custom_user = get_user_model()
        user = custom_user.objects.create_user(username='testuser', password='12345')
        self.create_itinerary('Guide to Florida', user, False)
        self.create_itinerary('Guide to Tokyo', user, False)
        self.create_itinerary('Blueridge Weekend Tour', user, True)

class GetAllItinerariesTest(BaseViewTest):
    """
    GET all Itineraries Test
    """
    def test_get_all_itineraries(self):
        """
        Test that all Itinerary objects exist when we make a GET request
        to itinerary/ endpoint
        """

        response = self.client.get(
            reverse("itinerary-all")
        )
        expected = Itinerary.objects.all()
        serialized = ItinerarySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllPOIsTest(BaseViewTest):
    """
    GET all Points of Interest for an Itinerary
    """
    def test_get_itinerary_points(self):
        """
        Test that all POIs are returned for a given Itinerary
        """
        response = self.client.get('/itinerary/1')
        expected = Itinerary.objects.get(id=1)
        serialized = POISerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
