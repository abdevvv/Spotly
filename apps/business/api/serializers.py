from rest_framework import serializers


from apps.business.models import Business,Favorite,Category

class BusinessListSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    distance = serializers.CharField(required=False)
    class Meta:
        model = Business
        fields = ['id','name','location','distance']
    
    def get_location(self,obj):
        return [obj.location.x, obj.location.y] if obj.location else None

    
class BusinessDetailSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    distance = serializers.CharField(required=False)
    class Meta:
        model = Business
        fields = "__all__"
    
    def get_location(self,obj):
        return [obj.location.x, obj.location.y] if obj.location else None