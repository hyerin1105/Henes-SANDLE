from django.contrib import admin
from django.urls import path, include
from .views import login, join
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from management import views
from main import views

"""
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(next_page='wait'), name='logout'),
]
"""

app_name = 'management', 'main'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'),
    ### 로그아웃 추가 ####
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('join/', views.join, name='join'),
]