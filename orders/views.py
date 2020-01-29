from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import NewOrderForm
from customers.models import CustomerInfo

# Create your views here.

@login_required
def order_view(request):
    title_text = 'Orders'
    active_or = 'active'
   
    context = {'title_text': title_text, 'active_or': active_or}
    return render(request, 'orders/index.html', context)
    
@login_required
def new_order_view(request):
    form = NewOrderForm()
    title_text = 'New Order'
    active_or = 'active'
    customers = CustomerInfo.objects.all()
    

    if form.is_valid():
        form.save()
        form = NewOrderForm()
   
    context = {'title_text': title_text, 'active_or': active_or, 'form': form, 'customers': customers}
    return render(request, 'orders/new-order.html', context)
