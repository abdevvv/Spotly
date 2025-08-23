from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from apps.business.api.filters import BusinessFilter
from apps.business.models import Business
from apps.business.api.serializers import BusinessListSerializer, BusinessDetailSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusinessFilter
    def get_serializer_class(self):
        action = self.action
        if action == 'list':
            return BusinessListSerializer
        if action == 'retrieve':
            return BusinessDetailSerializer
    
 