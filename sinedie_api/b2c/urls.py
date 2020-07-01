from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('client/me/', RetrieveUpdateClient.as_view()),
    path('client/<int:pk>/', RetrieveClient.as_view()),
    path('client/create/', CreateClient.as_view()),
    path('client/bookings/', ListBooking.as_view()),
    path('client/favorites/', ListFavoriteBusiness.as_view()),
    path('client/location/', UpdateLocation.as_view()),
]