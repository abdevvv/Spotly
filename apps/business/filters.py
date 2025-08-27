from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


import django_filters



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
    
    def filter_by_distance(self, queryset, name, value):
        request = self.request
        lat = request.GET.get("lat")
        lng = request.GET.get("lng")
        radius = request.GET.get("radius")

        if not lat or not lng:
            return queryset

        user_point = Point(float(lng), float(lat), srid=4326)

        if not radius:
            qs =  queryset.annotate(
                distance=Distance("location", user_point)
            ).order_by("distance")
            return qs

        qs = queryset.filter(
            location__dwithin=(user_point, D(m=float(radius)))
        ).annotate(
            distance=Distance("location", user_point)
        ).order_by("distance")


        return qs