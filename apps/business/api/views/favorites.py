from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response


from apps.business.models import Favorite
from apps.business.api.serializers.favorite import FavoriteListSerializer,FavoriteCreateSerializer


class FavoriteList(generics.ListAPIView):
    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)
    

class FavoriteCreate(generics.CreateAPIView):
    serializer_class = FavoriteCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                "detail": "Business added to favorites successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )