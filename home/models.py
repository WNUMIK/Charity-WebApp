from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from . import enums


# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('Users must provide the Email.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
        )

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        # user_group = Group.objects.get(name='regular')
        # user.groups.add(user_group)
        return user

    def create_superuser(self, email, name, surname, password=None):
        user = self.create_user(email=email, name=name, surname=surname, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_join = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    type = models.IntegerField(choices=enums.STATUS, default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def get_categories(self):
        return "\n".join([c.name for c in self.categories.all()])


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=300)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    is_taken = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.email
