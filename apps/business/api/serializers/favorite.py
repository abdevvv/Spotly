from rest_framework.validators import ValidationError
from rest_framework import serializers


from apps.business.models import Business,Favorite
from apps.business.api.serializers.business import BusinessListSerializer


#Favorite
class FavoriteListSerializer(serializers.ModelSerializer):
    business = BusinessListSerializer()
    class Meta:
        model = Favorite
        fields = ['id','business']

class FavoriteCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    business = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'business']
        validators = []  

    def validate(self, attrs):
        #double check: check if exists, check if added to favorites already for the user
        user = attrs['user']
        business_id = attrs['business']
        
        # 1. exists?
        business = Business.objects.filter(id=business_id,is_activated=True)
        if not business.exists():
            raise ValidationError({'detail':"The business is not valid"})
        business = business.first()
     
        # 2. added to favorites?
        if Favorite.objects.filter(user=user, business=business).exists():
            raise ValidationError({'detail': "This Business had added to Favorites before"})
        
        attrs['business'] = business
        return attrs
