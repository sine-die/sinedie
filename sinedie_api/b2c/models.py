from django.db import models


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField('intermediate.User', on_delete=models.CASCADE, primary_key=True)
    favorites = models.ManyToManyField('b2b.Business')
    cur_postcode = models.CharField(max_length=5) # validators: nomes nums
    phone = models.CharField(max_length=9)