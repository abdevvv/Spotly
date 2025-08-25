from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point


import django_filters


from apps.business.models import Business

class BusinessFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    address = django_filters.CharFilter(field_name="address", lookup_expr="icontains")
    category = django_filters.NumberFilter(field_name="category_id")
     
    #GEO
    lat = django_filters.NumberFilter(method="filter_by_distance")
    lng = django_filters.NumberFilter(method="filter_by_distance")
    radius = django_filters.NumberFilter(method="filter_by_distance")
    class Meta:
        fields = ['name','category','address']
    
    def filter_by_distance(self,queryset, name, value):
        request = self.request
        lat = request.GET.get("lat")
        lng = request.GET.get("lng")
        radius = request.GET.get("radius")
        
        #first case: if no lat or lng return qs
        if not lat or not lng:
            return queryset
        
        user_point = Point(float(lng),float(lat), srid=4326)
        
        #second case if not radius return the user nearst location
        if not radius:
            return queryset.annotate(
                distance = Distance("location",user_point)
            ).order_by("distance")
        
        #3rd case return with radius
        qs = queryset.annotate(
            distance = Distance("location",user_point)
        ).filter(distance__lte=float(radius))
        return qs