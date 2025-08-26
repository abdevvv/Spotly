from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


from apps.business.permissions import IsBusinessOwner, IsOwner
from apps.business.filters import BusinessFilter
from apps.business.models import Business
from apps.business.api.serializers.business import BusinessListSerializer, BusinessDetailSerializer,BusinessCreateUpdateSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.filter(is_activated=True)
    filter_backends = [DjangoFilterBackend]
    filterset_class = BusinessFilter
    
    #serializer class
    def get_serializer_class(self):
        action = self.action
        print(action)
        #list
        if action == 'list':
            return BusinessListSerializer

        #retrieve
        if action == 'retrieve':
            return BusinessDetailSerializer

        #create and update and partial
        if action in ['create','update','partial_update',]:
            return BusinessCreateUpdateSerializer
    
    #permissions
    def get_permissions(self):
            #create
            if self.action == "create":
                permission_classes = [IsAuthenticated, IsOwner]
            
            #Update and partial and destroy
            elif self.action in ["update", "partial_update",'destroy']:
                permission_classes = [IsAuthenticated, IsBusinessOwner]
            
            #list ,..
            else:
                permission_classes = [IsAuthenticated] 
            return [permission() for permission in permission_classes]