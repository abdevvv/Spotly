from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from apps.business.api.filters import BusinessFilter
from apps.business.models import Business
from apps.business.api.serializers import BusinessSerializer

class BusinessList(generics.ListAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusinessFilter
