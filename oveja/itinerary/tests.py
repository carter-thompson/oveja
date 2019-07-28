from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Itinerary
from .serializers import ItinerarySerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_itinerary(title, owner, isPublished):
        Itinerary.objects.create(title, owner, isPublished)

    
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.create_itinerary('Guide to Florida', login, False)
        self.create_itinerary('Guide to Tokyo', login, False)
        self.create_itinerary('Blueridge Weekend Tour', login, True)


class GetAllItinerariesTest(BaseViewTest):
    
    def test_get_all_itineraries(self):
        """
        Test that all Itinerary objects exist when we make a GET request to itinerary/ endpoint
        """

        response = self.client.get(
            reverse("itinerary-all")
        )
        expected = Itinerary.objects.all()
        serialized = ItinerarySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)