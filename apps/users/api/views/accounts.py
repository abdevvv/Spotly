from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.api.serializers import UserSerializer

#for retrieve and update
class UserGeneric(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
