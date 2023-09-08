from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class Customer(models.Model):
    address = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.address




class UserManager(BaseUserManager):
    def create_user(self, password=None):

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, address, password):
        user = self.create_user(
            address,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    address = models.AddressField(
        verbose_name='address',
        max_length=15,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'address'

    def __str__(self):
        return self.address

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin