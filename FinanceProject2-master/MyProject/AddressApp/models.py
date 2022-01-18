from django.db import models
from Customer.models import Customer


# Create your models here.

class PermanentAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='paddress')
    flat_no = models.IntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.flat_no


class CurrentAddress(models.Model):
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE)
    flat_no_1 = models.IntegerField()
    street_name_1 = models.CharField(max_length=100)
    city_1 = models.CharField(max_length=100)
    pincode_1 = models.IntegerField()
    area_1 = models.CharField(max_length=100)
    landmark_1 = models.CharField(max_length=100, blank=True)
    district_1 = models.CharField(max_length=100)
    state_1 = models.CharField(max_length=100)
    country_1 = models.CharField(max_length=100)

    def __str__(self):
        return self.flat_no_1
