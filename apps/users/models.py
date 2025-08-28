from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager


# Create your models here.
class User(AbstractUser):
    gender_choices = (
        ("male", "Male"),
        ("female", "Female")
    )
    role_choices = (
        ("owner","Owner"),
        ("customer","Customer")
    )
    email = models.EmailField(max_length=80, unique=True)
    image = models.ImageField(upload_to='Photos/users/%y/%m/%d', null=True, blank=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    phoneNumber = models.CharField(null=True, blank=True, max_length=45)
    dateBirth = models.DateField(null=True, blank=True)
    role = models.CharField(choices=role_choices,default="customer")
    gender = models.TextField(null=True, blank=True, choices=gender_choices)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def is_owner(self):
        return self.role == "owner"

    


