from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from apps.business.models import Review
from apps.business.utilities import get_business
from apps.business.api.serializers.review import ReviewListSerializer,ReviewCreateSerializer

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        #make sure that business id is valid
        business_id = self.kwargs.get("business_id")
        business = get_business(business_id=business_id)
        
        return Review.objects.select_related("user").filter(business=business.id)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]