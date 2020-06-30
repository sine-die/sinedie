from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('signup/')
    path('business/', ListCreateBusiness.as_view()),
    path('business/<int:pk>/', RetrieveUpdateBusiness.as_view()),
    path('business/<int:business>/bookings/', ListBooking.as_view()),
    path('business/<int:pk>/capacity/', RetrieveUpdateCapacity.as_view()),
]