from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import CustomerInfo
# Create your views here.

def index(request):
    customer_list = CustomerInfo.objects.order_by('-last_name')
    context = {'customer_list' : customer_list}
    return render(request, 'customers/index.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(CustomerInfo, pk=customer_id)
    return render(request, 'customers/detail.html', {'customer': customer})