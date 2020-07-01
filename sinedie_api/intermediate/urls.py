from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('business/<int:business>/bookings/create/', CreateBooking.as_view()),
    path('business/<int:business>/bookings/<int:pk>/', RetrieveUpdateBooking.as_view()),
    path('business/<int:business>/queue/create/', CreateQueue.as_view()),
    path('business/<int:business>/queue/', ListQueue.as_view()),
    path('business/<int:business>/queue/<int:pk>/pop/', PopQueue.as_view()),
]