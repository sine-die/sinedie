from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('signup/')
    path('business/', ListCreateBusiness.as_view()),
    path('business/<int:pk>/', RetrieveUpdateBusiness.as_view()),
    path('business/<int:business>/bookings/', ListCreateBooking.as_view()),
    path('business/<int:business>/bookings/<int:pk>/', RetrieveUpdateBooking.as_view()),
    path('business/<int:business>/queue/', ListCreateQueue.as_view()),
    path('business/<int:business>/queue/pop/<int:pk>/', PopQueue.as_view()),
    path('business/<int:pk>/capacity/', RetrieveUpdateCapacity.as_view()),
]