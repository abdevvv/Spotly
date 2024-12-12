from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializers import LoginSerializer, UserSerializer

class LoginGeneric(generics.CreateAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer = self.serializer_class(data=data,context={'request':request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            message = {
                'detail':"Logged in Successfully",
                "data":serializer.data,
                'token':{
                'access':str(refresh.access_token),
                'refresh':str(refresh)
            },

            }
            return Response(message,status=status.HTTP_200_OK)
        message = {'detail':"something went wrong"}
        return Response(message,status=status.HTTP_200_OK)
    

class RegiserGeneric(generics.CreateAPIView):
    serializer_class = UserSerializer