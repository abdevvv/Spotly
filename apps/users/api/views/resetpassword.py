
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from apps.users.models import ResetPassword
from apps.users.api.serializers import ResetRequestSerializer,ResetPasswordSerializer
from apps.users.otp import OTPHandler

class EmailRequestGeneric(generics.CreateAPIView):
    queryset = ResetPassword.objects.all()
    serializer_class = ResetRequestSerializer
        

class ResetPasswordGeneric(generics.CreateAPIView):
    serializer_class = ResetPasswordSerializer



@api_view(["POST"])
def check_otp(request):
    #otp and reset_token is required
    otp = request.data.get("otp")
    reset_token = request.data.get("token")

    #method 1: check otp and reset_token avalibality
    if not otp or not reset_token:
        message = {
            'detail':"The otp and reset password token is required"
        }
        raise ValidationError(message)
    
    #method 2: check otp and reset token for the same obj and if reset_token is_available
    reset_obj = ResetPassword.objects.filter(token=reset_token,is_checked=False)
    if not reset_obj.exists():
        message = {
            'detail':"The OTP is not found"
        }
        raise ValidationError(message)
    otphandler = OTPHandler(reset_token=reset_token)
    if not otphandler.check_otp(otp=otp):
        raise ValidationError({'detail':"The OTP is not valid"})
    
    obj = reset_obj.first()
    if not obj.is_available():
        message = {
            'The request operation time out, try again'
        }
        raise ValidationError(message)
    
    #method 3: set checked to true and remove the otp
    obj.is_checked = True
    obj.save()
    # otphandler.delete_otp()
    message = {
        'detail':"The OTP is valid ."
    }
    return Response(data=message,status=status.HTTP_200_OK)