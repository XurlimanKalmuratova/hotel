from django.contrib.admin import *
from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(ModelAdmin):
    list_display = ('id', 'number')
    list_display_links = ('id', 'number')