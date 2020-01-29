from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.fields.CharField(max_length=32)
    last_name = models.fields.CharField(max_length=32)

    phone_number = PhoneNumberField()
    home_phone = PhoneNumberField(null=True, blank=True)
    business_phone = PhoneNumberField(null=True, blank=True)

    address = models.fields.CharField(max_length=64)
    city = models.fields.CharField(max_length=32)
    state = models.fields.CharField(max_length=2)
    zipcode = models.fields.PositiveSmallIntegerField()
