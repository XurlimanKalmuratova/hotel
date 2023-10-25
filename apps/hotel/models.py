
from django.db.models import *

class Hotel(Model):
    name = CharField(max_length=256)
    address = CharField(max_length=256)
    city = CharField(max_length=256)
    country = CharField(max_length=256)
    rating = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    
        