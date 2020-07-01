from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('signup/')
    path('business/me/', RetrieveBusiness.as_view()),
    path('business/', ListCreateBusiness.as_view()),
    path('business/<int:pk>/', RetrieveUpdateBusiness.as_view()),
    path('business/bookings/', ListBooking.as_view()),
    path('business/queue/', ListQueue.as_view()),
    path('business/<int:pk>/capacity/', RetrieveUpdateCapacity.as_view()),
]