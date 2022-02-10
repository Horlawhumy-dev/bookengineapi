from typing import List
from rest_framework import serializers
from .models import BlockedDay, BookingInfo, Listing

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockedDay
        # fields = "__all__"
        exclude = ('check_in', 'check_out', 'max_price')



class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingInfo
        fields = "__all__"
        # exclude = ('listing',)



class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = "__all__"
        # exclude = ('id',)