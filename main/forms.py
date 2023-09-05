from django import forms
from .models import Customer
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('password', )