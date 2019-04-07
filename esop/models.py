from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    role = models.IntegerField(default=0)
# Customer = 1 and Seller = 2

class Customer(models.Model):
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    # phone = PhoneNumberField(null=False, blank=False, unique=True)

class Seller(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    # phone = PhoneNumberField(null=False, blank=False, unique=True)
