from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import User
from django.contrib import auth
from main.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView

def join(request):
    if request.method == "POST":
        new_user = User.objects.create_user(address=request.POST['address'], password=request.POST['password'])
        auth.login(request, new_user)
        return redirect('goods')
        
    return render(request, 'join.html')

def login(request):
    if request.method == "POST":
        address=request.POST.get('address',None)
        password=request.POST.get('password',None)
        user=auth.authenticate(request, address=address, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('goods')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'management/login.html')

def logout(request):
    if request.session.get('customer'):
        del(request.session['customer'])
    return redirect('/')