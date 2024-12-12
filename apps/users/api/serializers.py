from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework.validators import ValidationError


from apps.users.otp import OTPHandler
from apps.users.models import User, ResetPassword
from apps.users.tasks import send_email

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(required=True,max_length=128, style={"input_type": "password"},write_only=True)
    is_activated = serializers.BooleanField(required=False,read_only=True)
    class Meta:
        fields = ['email','password','is_activated']
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(email=email,password=password)
        if not user:
            raise ValidationError({'detail':"The email or password is not valid ."})

        if not user.is_activated:
            raise ValidationError({'detail':"the user is not activated"})
        
        attrs['user'] = user
        attrs['is_activated'] = user.is_activated

        return attrs

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(required=True,max_length=128, style={"input_type": "password"},write_only=True)
    is_activated = serializers.BooleanField(required=False,read_only=True)
    class Meta:
        model = User
        fields = ['email',"username","password","phoneNumber",'image',"dateBirth","gender","is_activated",]
    def validate(self, attrs):
        #check if email exists
        email = attrs.get("email")
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError({'detail':"The user email had been used, try another email"})
        return attrs
    def create(self, validated_data):
        #change user passwd to encrypted passwd
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    


class ResetRequestSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    user = serializers.CharField(required=False,)
    email = serializers.CharField(write_only=True)
    class Meta:
        model = ResetPassword
        fields = ['user','token','email']
    
    def validate(self, attrs):
        #method1 : check user_email
        email = attrs.get('email')
        try:
            user = User.objects.get(email=email)
        except:
            message = {
                'detail':"the email is not valid"
            }
            raise ValidationError(message)
        #define user and pop email after checking
        attrs['user'] = user
        attrs.pop('email')
        return attrs
    def create(self, validated_data):
        obj = super().create(validated_data)
        #define otp
        otp_handler = OTPHandler(reset_token=obj.token)
        otp = otp_handler.create_otp_for_user()
        #send email message
        send_email.delay(user_email=obj.user.email,user_otp=otp)
        return obj



class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        token = attrs.get('token')
        #method 1: check if the token is valid and is checked
        reset_obj = ResetPassword.objects.filter(token=token,is_checked=True)
        if not reset_obj.exists():
            message = {
                'detail':"The token is not valid"
            }
            raise ValidationError(message)
    
        #method 2: check if the token is still available
        obj = reset_obj.first()
        if not obj.is_available():
            message = {
                'detail':"sorry this operation timedout, try again"
            }
            raise ValidationError(message)

        #define user
        attrs['user'] = obj.user

        #method 3: delete reset_password obj
        obj.delete()
        return super().validate(attrs)
    
    def create(self, validated_data):
        #change password
        user:User = validated_data['user']
        password = validated_data['new_password']
        user.set_password(password)
        user.save()
        RefreshToken.for_user(user=user)
        return ""
    
    def to_representation(self, instance):
        return {
            'detail':"The Password reseted successfully ."
        }
    
