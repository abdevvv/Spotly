from rest_framework import serializers
from rest_framework.validators import ValidationError

from apps.business.models import Review
from apps.business.utilities import get_business


class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id','user','rate','comment','created_at']

    #username
    def get_user(self,obj):
        return obj.user.username
    

#rate validation
#business validation
#user and business should be unique together

class ReviewCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    business = serializers.IntegerField(write_only=True)
    rate = serializers.IntegerField()
    comment = serializers.CharField()
    
    def validate(self, attrs):
        rate = attrs["rate"]
        business_id = attrs['business']
        user = self.context['request'].user
        #1. validate rate
        if rate > 5:
            raise ValidationError({'detail':"the value of rate field shouldn`t be more than 5"})
        
        #2. check business and return it
        business = get_business(business_id=business_id)

        #3. check the business and user didn`t have a record together in review
        review = Review.objects.filter(business=business_id,user=user)
        if review.exists():
            raise ValidationError({'detail':"the user has already rated the business before "})
        
        #define values
        attrs["business"] = business
        attrs['user']= user
        return attrs
    

    def create(self, validated_data):
        return Review.objects.create(**validated_data)