from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import ValidationError


from apps.users.models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(required=True,max_length=128, style={"input_type": "password"},write_only=True)
    role = serializers.CharField(read_only=True)
    class Meta:
        fields = ['email','password','is_activated']
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        user = authenticate(email=email,password=password)
        if not user:
            raise ValidationError({'detail':"The email or password is not valid ."})

        attrs['user'] = user
        attrs["role"] = user.role

        return attrs

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(required=True,max_length=128, style={"input_type": "password"},write_only=True)
    class Meta:
        model = User
        fields = ['email',"username","password","phoneNumber",'image',"dateBirth","gender","role"]
    def validate(self, attrs):
        #check if email exists
        email = attrs.get("email")
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
    

