from rest_framework import generics

from apps.users.permissions import IsActivated
from apps.users.api.serializers import UserSerializer

#for retrieve and update
class UserGeneric(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsActivated]
    def get_object(self):
        return self.request.user
