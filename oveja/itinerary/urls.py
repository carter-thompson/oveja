from django.urls import path
from .views import ListItinerariesView, ItineraryDetail

urlpatterns = [
    path('itinerary/', ListItinerariesView.as_view(), name="itinerary"),
    path('itinerary/<int:pk>', ItineraryDetail.as_view(), name='itinerary-detail')
]
