from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import CustomerInfo
from .forms import NewCustomerForm
# Create your views here.

@login_required
def index(request):
    customer_list = CustomerInfo.objects.order_by('id')
    title_text = 'Customers'
    
    context = {'customer_list' : customer_list, 'title_text': title_text}
    return render(request, 'customers/index.html', context)

@login_required  
def detail(request, customer_id):
    customer = get_object_or_404(CustomerInfo, pk=customer_id)
    title_text = 'Customer Details'

    context = {'customer': customer, 'title_text': title_text}
    return render(request, 'customers/detail.html', context)

@login_required    
def new_customer(request):
    form = NewCustomerForm(request.POST or None)
    title_text = 'New Customer'
    if form.is_valid():
        form.save()
        form = NewCustomerForm()
        
    context = {'form': form, 'title_text': title_text}
    return render(request, 'customers/new_customer.html', context)     