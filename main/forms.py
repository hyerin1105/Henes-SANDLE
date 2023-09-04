from django import forms
from .models import Customer
from django.contrib.auth.models import User

class ClForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].label = '주소'
        self.fields['password'].label = "비밀번호"
        self.fields['address'].widget.attrs.update({
            'class' : 'cl_address',
            'placeholder' : '주소',
        })
        self.fields['password'].widget.attrs.update({
            'class' : 'cl_password_form',
        })

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password']

class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['username','password']