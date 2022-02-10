from pprint import pprint
from django.urls import path
from .views import ReservationView, ListingView

urlpatterns = [
    path('units/', ReservationView.as_view(), name="reservationview"),
    path('list/', ListingView.as_view(), name="listingview"),

]