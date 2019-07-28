from django.urls import path
from .views import ListItineraryView

urlpatterns = [
    path('itinerary/', ListItineraryView.as_view(), name="itinerary-all"),
]
