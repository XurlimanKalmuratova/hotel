from django.db.models import *
from apps.guest.models import Guest
from apps.room.models import Room
class Booking(Model):
    room = ForeignKey(Room, on_delete=CASCADE)
    guest = ForeignKey(Guest, on_delete=CASCADE)
    check_in_date = DateField(auto_now=True)
    check_out_date = DateField(auto_now_add=False)
    is_paid = BooleanField(default=False)

    def __str__(self):
        return f'{self.room}'
    
    