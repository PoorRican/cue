from django.forms import ModelForm

from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'home_phone', 'business_phone',
                  'address', 'city', 'state', 'zipcode']
