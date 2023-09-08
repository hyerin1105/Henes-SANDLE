from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from management import views

"""
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(next_page='wait'), name='logout'),
]
"""

app_name = 'management'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='wait'), name='logout'), # 로그아웃 추가
    path('join/', views.join, name='join'),
]