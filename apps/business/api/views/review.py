from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.validators import ValidationError


from apps.business.models import Review, Business
from apps.business.api.serializers.review import ReviewListSerializer,ReviewCreateSerializer

class ReviewList(generics.ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        #make sure that business id is valid

        business_id = self.kwargs.get("business_id")
        business = Business.objects.filter(id=business_id,is_activated=True)
        if not business.exists():
            raise ValidationError({'detail':"The business is not valid"})
        
        business = business.first()
        print(business.review__rate)
        
        return Review.objects.select_related("user").filter(business=business.id)

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]