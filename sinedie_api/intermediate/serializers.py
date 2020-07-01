from rest_framework import serializers
from intermediate.models import Booking, Queue


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['business', 'client']
        #optional_fields = ['favorites', 'cur_postcode']


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'
        read_only_fields = ['business', 'client']