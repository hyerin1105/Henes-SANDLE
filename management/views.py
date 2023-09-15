from django.shortcuts import render, redirect
from main.models import Customer
#from main.views import customer_id
from django.contrib.auth import get_user_model  # get_user_model 변수로 데이터베이스 조회 가능
from django.http import HttpResponse  # 화면에 텍스트를 띄워주기 위함
from django.contrib import auth  # 유저 정보 검증하기 위함
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  # 데코레이터 함수 생성


def signup(request):  # 회원가입 함수
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = Customer.objects.create_user(address=request.POST['address'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')

            
# 로그인
@csrf_exempt
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        address = request.POST['address']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        customer = auth.authenticate(request, address=address, password=password)
        
        # 해당 user 객체가 존재한다면
        if customer is not None:
            # 로그인한다
            auth.login(request, customer)
            return redirect('goods')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

# 로그아웃
@login_required  # 로그인 인증되어있을 때만 실행됨
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    auth.logout(request)
    return redirect('/')