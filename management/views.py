from django.shortcuts import render, redirect
from main.models import Customer
from django.contrib.auth import get_user_model  # get_user_model 변수로 데이터베이스 조회 가능
from django.http import HttpResponse  # 화면에 텍스트를 띄워주기 위함
from django.contrib import auth  # 유저 정보 검증하기 위함
from django.contrib.auth.decorators import login_required  # 데코레이터 함수 생성


def sign_up_view(request):  # 회원가입 함수
    if request.method == 'GET':
        return render(request, 'join.html')
    elif request.method == 'POST':  # 회원가입 정보 입력 후 가입하기 클릭시
        address = request.POST.get('address', None)  # 이름
        password = request.POST.get('password', None)  # 비밀번호
        password2 = request.POST.get('password2', None)  # 비밀번호 확인

        if password != password2:  # 비밀번호와 비밀번호 확인이 같지 않으면
            return render(request, 'join.html')  # 페이지 다시 로드
        
        else:  # 같으면
            Customer.objects.create_user(address=address, password=password)  # 데이터베이스에 이름, 비밀번호, 자기소개를 저장
            return redirect('main.html')  # 고객용 메인 페이지로 이동
            
def sign_in_view(request):
    if request.method == 'POST':
        address = request.POST.get('address', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, address=address, password=password)
        # auth.authenticate() 로 암호화된 데이터베이스를 추가적인 코드없이 조회 및 검증이 가능
        
        if me is not None:  # 입력한 정보가 존재하고 일치한다면
            auth.login(request, me)  # auth.login() 으로 토큰을 생성 및 전달
            return HttpResponse(address + '님 환영합니다')
        else:  # 입력한 정보가 없거나 틀리다면
            return redirect('management/login')  # 페이지 다시 로드
    elif request.method == 'GET':
        return render(request, 'management/join.html')
    
@login_required  # 로그인 인증되어있을때만 실행됨
def logout(request):
    auth.logout(request)  # 장고 내장 기능인 로그아웃
    return redirect('/')