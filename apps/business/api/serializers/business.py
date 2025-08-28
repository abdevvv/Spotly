from django.contrib.gis.geos import Point


from rest_framework import serializers


from apps.business.models import Business, Category

#categories
class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ["id","title"]


class BusinessListSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    distance = serializers.CharField(required=False)
    class Meta:
        model = Business
        fields = ['id','name','location','distance',"category",'rate_avg']
    
    #[x,y]
    def get_location(self,obj):
        return [obj.location.x, obj.location.y] if obj.location else None

    
class BusinessDetailSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
    category = BusinessCategorySerializer()
    distance = serializers.CharField(required=False)
    class Meta:
        model = Business
        fields = "__all__"
    
    #[x,y]
    def get_location(self,obj):
        return [obj.location.x, obj.location.y] if obj.location else None



class BusinessCreateUpdateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location = serializers.ListField()
    is_activated = serializers.BooleanField(read_only=True)
    class Meta:
        model = Business
        fields = "__all__"

    #validate location to return from list to Point()
    def validate_location(self, value):
        if isinstance(value, (list, tuple)) and len(value) == 2:
            lng, lat = value
            return Point(lng, lat, srid=4326)
        return value
    
