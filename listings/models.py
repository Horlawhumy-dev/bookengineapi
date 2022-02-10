from re import T
from django.db import models
from datetime import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)

    def __str__(self):
        return self.title
    

class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_room_types'
    )
    title = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.hotel} - {self.title}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_rooms'
    )
    room_number = models.CharField(max_length=255,)

    def __str__(self):
        return self.room_number


class BookingInfo(models.Model):
    listing = models.OneToOneField(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )
    hotel_room_type = models.OneToOneField(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type
            
        return f'{obj} {self.price}'


class BlockedDay(models.Model):
    booking_info = models.ForeignKey(BookingInfo, on_delete=models.CASCADE)
    max_price = models.IntegerField(null=True, blank=True)
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(null=True, blank=True)


    def save(self, *args, **kwargs):
        n = 3 # 3months interval
        given_date = self.check_in #default would be => datetime.now
        date_format = '%Y/%m/%d'
        dtObj = datetime.strptime(given_date.strftime(date_format), date_format)
        future_date = (dtObj + relativedelta(months=n)).date() #format would be => '2022-02-10'
        self.check_out = future_date

        if self.booking_info[1] == 'Apartment':
            self.max_price = 0
        else:
            self.max_price = 100

        return super(BlockedDay, self).save(*args, **kwargs)