from django.contrib import admin
from django.urls import path, include
from .views import login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', LogoutView.as_view(next_page='wait'), name='logout'),
]