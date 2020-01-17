import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class CustomerInfo(models.Model):
    business_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    landline = models.CharField(max_length=200)
    email_1 = models.CharField(max_length=200)
    email_2 = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    referral = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)

    # Idenitfy self
    def __str__(self):
        return self.first_name + ' ' + self.last_name