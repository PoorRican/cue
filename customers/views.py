from django.shortcuts import render

from .forms import CustomerForm


def new_customer(request):
    if request.method == 'GET':
        form = CustomerForm()
        context = {'form': form}
        return render(request, 'new_customer.html', context)
