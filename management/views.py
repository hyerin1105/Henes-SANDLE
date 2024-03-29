from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  # 데코레이터 함수 생성
from django.contrib.auth.hashers import make_password, check_password

# 회원가입
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        confirm = request.POST.get('confirm', None)

        err_data = {}
        if not (username and password and confirm):
            err_data['error'] = 'every'

        elif password != confirm:
            err_data['error'] = 'different'
        
        else:
            customer = User(
                username=username,
                password=make_password(password),
            )
            customer.save()
            return redirect('checking')
    return render(request, 'signup.html', err_data)

# 로그인
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        err_data = {}
        if not (username and password):
            err_data['error'] = '모든 값을 입력해 주세요.'
        else:
            customer = User.objects.get(username=username)
            if check_password(password, customer.password):
                request.session['user'] = customer.id
                return redirect('products')
            else:
                err_data['error'] = '비밀번호가 일치하지 않습니다.'
        return render(request, 'signup.html', err_data)

# 로그아웃
#@login_required 로그인 인증되어있을 때만 실행됨
def logout(request):
    auth.logout(request)
    return redirect('wait')
