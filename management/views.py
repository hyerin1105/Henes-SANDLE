from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib.auth.views import LoginView
from django.contrib import auth
from main.forms import UserForm
from main.forms import LoginForm
from django.contrib.auth.views import LogoutView

def login(request):
    if request.method == "POST":
        password=request.POST.get('password',None)
        user=auth.authenticate(request, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'login.html')