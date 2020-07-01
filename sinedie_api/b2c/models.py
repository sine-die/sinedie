from django.db import models


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField('intermediate.User', on_delete=models.CASCADE, primary_key=True)
    favorites = models.ManyToManyField('b2b.Business', blank=True)
    cur_postcode = models.CharField(max_length=5, blank=True, null=True) # validators: nomes nums