from django.shortcuts import render
from .models import Booking, Queue, User
from .serializers import BookingSerializer, QueueSerializer
from rest_framework import generics, permissions
from b2b.models import Business
from b2c.models import Client
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
######################
### BOOKINGS VIEWS ###
######################
class CreateBooking(generics.CreateAPIView):
    # todo: crear permission isOwnerOrWriteOnly
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        business = Business.objects.get(pk=self.kwargs['business'])
        client = self.request.user.client if hasattr(self.request.user, 'client') \
            else Client.objects.get(user__username='anonymous')
        serializer.save(business=business, client=client, **serializer.validated_data)


class RetrieveUpdateBooking(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(business=self.kwargs['business']).all()


####################
### QUEUES VIEWS ###
####################
class CreateQueue(generics.ListCreateAPIView):
    # todo: crear permission isOwnerOrWriteOnly
    serializer_class = QueueSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        business = Business.objects.get(pk=self.kwargs['business'])
        client = self.request.user.client if hasattr(self.request.user, 'client') \
            else Client.objects.get(user__username='anonymous')
        serializer.save(
            business=business, client=client,
            **serializer.validated_data
        )


class PopQueue(APIView):
    # todo: crear permission isOwner
    permission_classes = [permissions.AllowAny]

    def get(self, request, business, pk, format=None):
        q = Queue.objects.filter(pk=pk).update(active=False)
        return Response()


class ListQueue(APIView):
    # todo: crear permission isOwnerOrWriteOnly
    #serializer_class = QueueSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, business, format=None):
        return Response(
            {
                'people_waiting': Queue.objects.filter(business=business, active=True).count()
            }
        )