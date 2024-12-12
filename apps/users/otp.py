from django.core.cache import cache

from apps.users.models import ResetPassword

from rest_framework.validators import ValidationError
import random


class OTPHandler:
    def __init__(self, reset_token) -> None:
        #key of otp
        self.reset_token = reset_token

    def create_otp_for_user(self):
        rand_otp = self.generate_otp_code()
        cache.set(key=self.reset_token,value=rand_otp,timeout=300)
        return rand_otp

    def get_otp_for_user(self):
        return cache.get(key=self.reset_token)
    
    def check_otp(self,otp):
        #method 1: check if the otp is valid
        inputed_otp = otp
        valid_otp = self.get_otp_for_user()
        if not valid_otp:
            return False
        return inputed_otp == valid_otp
    
    def delete_otp(self):
        return cache.delete(key=self.reset_token)

    def generate_otp_code(self):
        number_list = [x for x in range(10)] 
        code_items_for_otp = []
        for i in range(5):
            num = random.choice(number_list)
            code_items_for_otp.append(num)
        code_string = "".join(str(item)for item in code_items_for_otp)
        return code_string
    