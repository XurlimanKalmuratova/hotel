from django.db.models import *

class Guest(Model):
    name = CharField(max_length=256)
    surname = CharField(max_length=256)
    email = CharField(max_length=256)
    phone = CharField(max_length=256)

    def __str__(self):
        return self.name