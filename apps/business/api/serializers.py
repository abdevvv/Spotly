from rest_framework import serializers


from apps.business.models import Business,Favorite,Category

class BusinessSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    class Meta:
        model = Business
        fields = ['name','location']
    
    def get_location(self,obj):
        return [obj.location.x, obj.location.y] if obj.location else None