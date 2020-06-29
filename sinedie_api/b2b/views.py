from django.shortcuts import render
from django.contrib.auth.views import SuccessURLAllowedHostsMixin
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ListCreateBusiness(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]


class RetrieveUpdateBusiness(generics.RetrieveUpdateAPIView):
    # todo: crear permission isOwnerOrReadOnly
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.AllowAny]


class ListCreateBooking(generics.ListCreateAPIView):
    # todo: crear permission isOwnerOrWriteOnly
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(business=self.kwargs['business']).all()

    def perform_create(self, serializer):
        business = Business.objects.get(pk=self.kwargs['business'])
        serializer.save(business=business, **serializer.validated_data)


class RetrieveUpdateBooking(generics.RetrieveUpdateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Booking.objects.filter(business=self.kwargs['business']).all()


class ListCreateQueue(generics.ListCreateAPIView):
    # todo: crear permission isOwnerOrWriteOnly
    serializer_class = QueueSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Queue.objects.filter(business=self.kwargs['business'], active=True).all()

    def perform_create(self, serializer):
        business = Business.objects.get(pk=self.kwargs['business'])
        serializer.save(business=business, **serializer.validated_data)


class PopQueue(APIView):
    # todo: crear permission isOwner
    permission_classes = [permissions.AllowAny]

    def get(self, request, business, pk, format=None):
        q = Queue.objects.filter(pk=pk).update(active=False)
        return Response()


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