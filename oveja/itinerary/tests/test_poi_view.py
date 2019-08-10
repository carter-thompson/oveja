"""
Tests for Itinerary with Points of Interest
"""

from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from ..models import Itinerary, POI
from ..serializers import ItinerarySerializer


class BaseViewTest(APITestCase):
    """
    Base View Test
    """
    client = APIClient()
    itinerary = None

    @staticmethod
    def create_itinerary(title, owner, is_published):
        """
        Create itinerary object
        """
        itinerary = Itinerary.objects.create(title=title, owner=owner, is_published=is_published)
        return itinerary

    @staticmethod
    def create_poi(**kwargs):
        """
        Create POI object
        """
        POI.objects.create(**kwargs)

    def setUp(self):
        """
        Setup
        """
        custom_user = get_user_model()
        user = custom_user.objects.create_user(username='testuser', password='12345')
        self.itinerary = self.create_itinerary('Guide to Florida', user, False)
        self.create_poi(
            itinerary=self.itinerary,
            name='start',
            latitude=27.992767,
            longitude=-82.448197,
            order=1
        )
        self.create_poi(
            itinerary=self.itinerary,
            name='end',
            latitude=27.996992,
            longitude=-82.448208,
            order=2
        )

class GetItineraryDetailsTest(BaseViewTest):
    """
    Test GET Itinerary
    """
    def test_get_itinerary_details(self):
        """
        Test that an Itinerary returns all POIs
        """
        response = self.client.get(
            reverse("itinerary-detail", kwargs={'pk': self.itinerary.id})
        )
        expected = Itinerary.objects.get(pk=self.itinerary.id)
        serialized = ItinerarySerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
