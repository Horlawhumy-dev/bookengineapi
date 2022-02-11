from asyncio.windows_events import NULL
from django.shortcuts import render
import json
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views  import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReservationSerializer, BookingSerializer, ListingSerializer
from .models import BlockedDay, BookingInfo, Listing, HotelRoomType
from itertools import chain

from django.core import serializers

# Create your views here.
class ReservationView(ListAPIView):
    queryset = BookingInfo.objects.all()
    serializer_class = BookingSerializer



# class ListingView(ListAPIView):
#     queryset = Listing.objects.all()
#     serializer_class = ListingSerializer




class ListingView(APIView):
    # queryset = Listing.objects.all()
    # serializer_class = ListingSerializer

    def get(self, request, format=None):
        booking = BookingInfo.objects.all()
        result = []
        info = None
        for book in booking:
            if book.listing:
                info = book.listing
            else:
                info = book.hotel_room_type
                # listing = HotelRoomType.objects.get(id=info.id)
                # result.append(listing)
        listing = Listing.objects.get(id=info.id)
        result.append(listing)
        data = result.append(booking)
        # serializers.serialize('json', booking) + serializers.serialize('json', result)

        return Response({
            "items": json.loads(data)
        }, status.HTTP_200_OK)
        
