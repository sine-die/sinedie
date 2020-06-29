from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)

BUSINESS_TYPES = [
    (0, 'bar'), (1, 'restaurant'),
    (2, 'shop'), (3, 'gym'),
    (4, 'other')
]

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=200)
    #bookings = models.ManyToManyField('Bookings', on_delete=models.CASCADE, through='Booking')
    max_capacity = models.IntegerField()
    cur_capacity = models.IntegerField()
    business_type = models.CharField(max_length=200, choices=BUSINESS_TYPES)
    description = models.TextField()
    #queue = models.OneToManyField('')

    class Meta:
        db_table = 'business_users'


class Booking(models.Model):
    client = models.IntegerField() # todo canviar per foreign key
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    canceled = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookings'


class Queue(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='queue')
    active = models.BooleanField(default=True)
    client = models.CharField(max_length=100) # todo canviar per foreign key

    class Meta:
        db_table = 'queue'