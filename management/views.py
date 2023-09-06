from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, join
from django.contrib.auth.forms import User
from django.contrib import auth
from main.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView

def join(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'management/join.html', {'form': form})

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