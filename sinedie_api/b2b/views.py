from django.shortcuts import render
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from intermediate.serializers import BookingSerializer, QueueSerializer
from intermediate.models import Booking, Queue
from datetime import datetime as dt


# Create your views here.
######################
### BUSINESS VIEWS ###
######################
class ListCreateBusiness(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['postcode']


class RetrieveUpdateBusiness(generics.RetrieveUpdateAPIView):
    # todo: crear permission isOwnerOrReadOnly
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]


class RetrieveBusiness(generics.RetrieveUpdateAPIView):
    # todo: crear permission isOwnerOrReadOnly
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.request.user.business


######################
### BOOKINGS VIEWS ###
######################
class ListBooking(generics.ListCreateAPIView):
    # todo: crear permission isOwner
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(
            business=self.request.user.business,
            date__gte=dt.now().date(), time__gte=dt.now().time()
        ).all()


class ListQueue(generics.ListCreateAPIView):
    # todo: crear permission isOwner
    serializer_class = QueueSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Queue.objects.filter(
            business=self.request.user.business,
            active=True
        ).all()


######################
### CAPACITY VIEWS ###
######################
class RetrieveUpdateCapacity(APIView):
    # todo: crear permission isOwner
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        out = Business.objects.values('max_capacity', 'cur_capacity').filter(pk=pk)
        return Response(out)

    def post(self, request, pk, format=None):
        business = Business.objects.get(pk=pk)
        cur_capacity = int(business.cur_capacity)
        incr = int(request.data.get('increase', 0))
        decr = int(request.data.get('decrease', 0))
        business.cur_capacity = cur_capacity + incr - decr
        print(cur_capacity, incr, decr)
        business.save()
        return Response({'cur_capacity': business.cur_capacity})