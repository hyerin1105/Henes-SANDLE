from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required

########### ceo ###########
def wait(request):
    return render(request, 'wait.html')

def loading(request):
    return render(request, 'loading.html')

def checking(request):
    return render(request, 'checking.html')

########### customer ###########
def main(request):
    return render(request,'main.html')

# @login_required(login_url='managment/login/')
def goods(request):
    return render(request, 'goods.html')

def complete(request):
    return render(request,'complete.html')

def end(request):
    return render(request, 'end.html')