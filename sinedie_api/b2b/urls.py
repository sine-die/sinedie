from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('signup/')
    path('business/<int:pk>/', RetrieveBusiness.as_view()),
    path('business/<int:pk>/bookings/', ListBookings.as_view()),
    path('business/<int:pk>/queue/', ListQueue.as_view()),
    path('business/<int:pk>/capacity/', RetrieveCapacity.as_view()),
]