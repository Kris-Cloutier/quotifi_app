from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import CustomerInfo
from .forms import MyCommentForm
# Create your views here.

def index(request):
    customer_list = CustomerInfo.objects.order_by('-last_name')
    context = {'customer_list' : customer_list}
    return render(request, 'customers/index.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(CustomerInfo, pk=customer_id)
    return render(request, 'customers/detail.html', {'customer': customer})
    
def new_customer(request):
    form = MyCommentForm(request.POST or None)
    title_text = 'New Customer'
    if form.is_valid():
        form.save()
        form = MyCommentForm()
        
    context = {'form': form, 'title_text': title_text}
    return render(request, 'customers/new_customer.html', context)     