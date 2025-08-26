from django.contrib.gis.geos import Point


from rest_framework.validators import ValidationError
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

class BusinessCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location = serializers.ListField()

    class Meta:
        model = Business
        fields = "__all__"

    #validate location to return from list to Point()
    def validate_location(self, value):
        if isinstance(value, (list, tuple)) and len(value) == 2:
            lng, lat = value
            return Point(lng, lat, srid=4326)
        return value
    