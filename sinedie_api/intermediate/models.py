from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_business = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)


class Booking(models.Model):
    client = models.ForeignKey('b2c.Client', on_delete=models.CASCADE, related_name='bookings')
    business = models.ForeignKey('b2b.Business', on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    canceled = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    num_people = models.IntegerField()

    class Meta:
        db_table = 'bookings'


class Queue(models.Model):
    business = models.ForeignKey('b2b.Business', on_delete=models.CASCADE, related_name='queue')
    active = models.BooleanField(default=True)
    client = models.ForeignKey('b2c.Client', on_delete=models.CASCADE, related_name='queue')
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'queue'