from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def product_view(request):
    title_text = 'Products'
    active_pr = 'active'
   
    context = {'title_text': title_text, 'active_pr': active_pr}
    return render(request, 'products/index.html', context)

@login_required
def new_product_view(request):
    title_text = 'New Product'
    active_pr = 'active'
   
    context = {'title_text': title_text, 'active_pr': active_pr}
    return render(request, 'products/new-product.html', context)