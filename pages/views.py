from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from customers.models import CustomerInfo

# Create your views here.
def index(request):
    # Importing customer data from customers app to display on pages app. 
    customer_list = CustomerInfo.objects.all()
    context = {'customer_list': customer_list}

    return render(request, 'pages/home.html', context)

def newCustomer(request):
    return render(request, 'pages/new-customer.html')  

def newOrder(request):
    return render(request, 'pages/new-order.html')      