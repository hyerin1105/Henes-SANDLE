from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib.auth.views import LoginView
from django.contrib import auth
from main.forms import UserForm
from main.forms import LoginForm
from django.contrib.auth.views import LogoutView

def login(request):
    if request.method == "POST":
        password=request.POST.get('password', None)
        user=auth.authenticate(request, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        return render(request, 'login.html')

"""    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        password = request.POST.get('password', None)

    res_data = ()

    if not(password):
        res_data['error'] = "비밀번호를 다시 입력해주세요."
    else:
        if check_password(password, customer.password):
            request.session['customer'] = customer.id
            return redirect('/')
        else:
            res_data['error'] = "비밀번호가 틀렸습니다."

    return render(request, 'login.html', res_data)
"""

def logout(request):
    if request.session.get('customer'):
        del(request.session['customer'])
    return redirect('/')