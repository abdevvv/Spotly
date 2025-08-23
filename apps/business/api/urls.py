from django.urls import path
from rest_framework.routers import DefaultRouter


from apps.business.api.views import business
router = DefaultRouter()
router.register(r'businesses', business.BusinessViewSet, basename='business')

urlpatterns = router.urls
