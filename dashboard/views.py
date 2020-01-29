from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard_view(request):
    title_text = 'Dashboard'
    active_ds = 'active'

    context = {'title_text': title_text,'active_ds': active_ds}
    return render(request, 'dashboard/index.html', context)