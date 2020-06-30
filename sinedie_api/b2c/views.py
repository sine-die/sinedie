from django.shortcuts import render
from intermediate.models import Booking, Queue
from intermediate.serializers import BookingSerializer, QueueSerializer
from rest_framework import generics, permissions
from datetime import datetime as dt
from .models import Client
from .serializers import ClientSerializer
from b2b.serializers import BusinessSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
####################
### CLIENT VIEWS ###
####################
class CreateClient(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]


class RetrieveUpdateClient(generics.RetrieveUpdateAPIView):
    # todo: crear permission isOwnerOrReadOnly
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Client.objects.filter(client__user__pk=self.request.user.pk)


######################
### BOOKINGS VIEWS ###
######################
class ListBooking(generics.ListCreateAPIView):
    # todo: crear permission isOwner
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(
            client=self.request.user.client, date__gte=dt.now().date(), time__gte=dt.now().time()
        ).all()


class ListFavoriteBusiness(generics.ListAPIView):
    serializer = BusinessSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return self.request.user.client.favorites.all()


class UpdateLocation(APIView):
    # todo: crear permission isOwner
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        request.user.client.cur_postcode = request.data['location']
        return Response()