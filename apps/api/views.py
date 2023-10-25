from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from apps.booking.models import Booking
from apps.guest.models import Guest
from apps.hotel.models import Hotel
from apps.room.models import  Room

from .serializer import *

class BookingAPIView(APIView):
    def get(self,request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class BookingDetailAPIView(APIView):
    def get(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request,pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=HTTP_204_NO_CONTENT)     
    



class GuestAPIView(APIView):
    def get(self,request):
        guests  = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        guests  = Guest.objects.all()
        serializer = GuestSerializer(guests, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class GuestDetailAPIView(APIView):
    def get(self, request, pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request,pk):
        guest = Guest.objects.get(pk=pk)
        serializer = GuestSerializer(guest,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        guest = Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=HTTP_204_NO_CONTENT)     



class HotelAPIView(APIView):
    def get(self,request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class HotelDetailAPIView(APIView):
    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request,pk):
        hotel  = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        hotel = Hotel.objects.get(pk=pk)
        hotel.delete()
        return Response(status=HTTP_204_NO_CONTENT)     



class RoomAPIView(APIView):
    def get(self,request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def post(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class RoomDetailAPIView(APIView):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def patch(self, request,pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(status=HTTP_204_NO_CONTENT)     
