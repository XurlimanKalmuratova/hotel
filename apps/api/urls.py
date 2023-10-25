from django.urls import path, include

from .views import *

urlpatterns = [
    path('room/', RoomAPIView.as_view()),
    path('room/<int:pk>/', RoomDetailAPIView.as_view()),
    path('hotel/', HotelAPIView.as_view()),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view()),
    path('guest/', GuestAPIView.as_view()),
    path('guest/<int:pk>/', GuestDetailAPIView.as_view()),
    path('booking/', BookingAPIView.as_view()),
    path('booking/<int:pk>/', BookingDetailAPIView.as_view()),

    path('auth/', include('dj_rest_auth.urls'))

]