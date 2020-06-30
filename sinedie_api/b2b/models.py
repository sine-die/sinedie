from django.db import models


class Business(models.Model):
    BUSINESS_TYPES = [
        (0, 'bar'), (1, 'restaurant'),
        (2, 'shop'), (3, 'gym'),
        (4, 'other')
    ]
    user = models.OneToOneField('intermediate.User', on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postcode = models.CharField(max_length=9)
    max_capacity = models.IntegerField()
    cur_capacity = models.IntegerField()
    business_type = models.CharField(max_length=200, choices=BUSINESS_TYPES)
    description = models.TextField()
    phone = models.CharField(max_length=9)

    class Meta:
        db_table = 'business_users'
