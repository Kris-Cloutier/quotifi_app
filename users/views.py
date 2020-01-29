from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    form = UserLoginForm()
    title_text = 'Log In'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    else:
        context = {
        'form': form,
        'title_text': title_text
    }
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    alert = messages.info(request, 'Logged out sucessfully!')

    context = {'alert': alert}
    return render(request, 'home.html', context)