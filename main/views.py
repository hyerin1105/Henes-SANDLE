from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
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
def main1(request):
    return render(request,'main.html')

@login_required(login_url='/login/')
def goods(request, customer_id): #views.py의 pk변수명과 urls.py의 변수명은 같아야 함
    customer = get_object_or_404(Customer, pk=customer_id) #모델과 pk를 customer_id라고 부를거야
    customer_form = LoginForm()
    return render(request,'goods.html', {'customer' : customer}) #값을 보낼거임

def complete(request):
    return render(request,'complete.html')

def end(request):
    return render(request, 'end.html')