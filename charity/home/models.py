from django.contrib.auth.models import User
from django.db import models

from . import enums


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Institution(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    type = models.IntegerField(choices=enums.STATUS, default=0)
    categories = models.ManyToManyField('Category', related_name='categories_institution')


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', related_name='donation_categories')
    institution = models.ForeignKey('Institution', related_name='institution_donation', on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=300)
    user = models.ForeignKey('User', default=Null, on_delete=models.CASCADE)