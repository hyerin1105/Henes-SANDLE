from django.contrib import admin
from .models import Customer

# Register your models here.
admin.site.register(Customer)

"""
from django.contrib import admin
from django.db import models

from .models import Customer

class Customer(models.Model):  # models.Model를 상속
    address = models.CharField(max_length=10, verbose_name='주소')  # admin 페이지에서 보일 컬럼명
    #5~7을 드래그 한뒤 Alt+Shift+Down하면 편함
    password = models.CharField(max_length=6, verbose_name='비밀번호')  # admin 페이지에서 보일 컬럼명

    #데이터가 문자열로 변환이 될 때 어떻게 나올지(반환해줄지) 정의하는 함수가 __str__이다.
    def __str__(self):
        return self.username

    #별도로 테이블명을 지정하고 싶을 때 쓰는 코드(안해도 됨)
    class Meta:
        db_table = 'user_define_customer_table' #테이블 명 지정
"""