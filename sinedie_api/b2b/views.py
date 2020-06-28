from django.shortcuts import render
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class RetrieveBusiness(generics.RetrieveAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]


class ListBookings(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(business=self.kwargs['pk']).all()


class ListQueue(generics.ListAPIView):
    serializer_class = QueueSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Queue.objects.filter(business=self.kwargs['pk']).all()


class RetrieveCapacity(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        out = Business.objects.values('max_capacity', 'cur_capacity').filter(pk=pk)
        return Response(out)