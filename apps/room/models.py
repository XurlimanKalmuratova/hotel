from django.db.models import *
from apps.hotel.models import Hotel
class Room(Model):

    hotel = ForeignKey(Hotel, on_delete=CASCADE)
    number = PositiveIntegerField()
    capacity = PositiveIntegerField()
    price_per_night = PositiveIntegerField()

    def __str__(self):
        return f'{self.number}'
