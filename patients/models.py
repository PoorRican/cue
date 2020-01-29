from django.db import models

from customers.models import Customer


class Patient(models.Model):
    SEX = ('M', 'F')
    SPECIES = ('Cat', 'Dog')

    owner = models.ForeignKey(Customer, related_name='pets', on_delete=models.PROTECT)

    name = models.fields.CharField('Patients Name', max_length=32)
    birth_date = models.fields.DateField()
    sex = models.fields.CharField(max_length=1, choices=SEX)
    neutered = models.BooleanField()
    species = models.fields.CharField(max_length=3, choices=SPECIES)
    breed = models.fields.CharField(max_length=64, null=True, blank=True)
    color = models.fields.CharField(max_length=32, null=True, blank=True)

    individual_needs = models.fields.TextField(null=True, blank=True)
    diet = models.fields.CharField(max_length=32, null=True, blank=True)
    coat_supplement = models.fields.CharField(max_length=32, null=True, blank=True)
    flea_treatment = models.fields.CharField(max_length=32)
    vitamins = models.fields.CharField(max_length=32)
    shampoo = models.fields.CharField(max_length=32)
