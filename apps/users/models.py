from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .manager import CustomUserManager

from datetime import timedelta, datetime

# Create your models here.
class User(AbstractUser):
    choices_gender = (
        ("male", "ذكر"),
        ("female", "أنثى")
    )
    email = models.EmailField(max_length=80, unique=True)
    image = models.ImageField(upload_to='Photos/users/%y/%m/%d', null=True, blank=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    phoneNumber = models.CharField(null=True, blank=True, max_length=45)
    dateBirth = models.DateField(null=True, blank=True)
    gender = models.TextField(null=True, blank=True, choices=choices_gender)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    

class ResetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=550,null=True,blank=True)
    is_checked = models.BooleanField(default=False)
    def save(self,*args, **kwargs):
        if not self.token:
            self.token = PasswordResetTokenGenerator().make_token(user=self.user)
        super().save(*args, **kwargs)
    
    def is_available(self):
        expiration_time = self.created_at + timedelta(minutes=10)
        return timezone.now() <= expiration_time
    
