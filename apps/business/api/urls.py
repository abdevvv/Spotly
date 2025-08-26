from django.urls import path
from rest_framework.routers import DefaultRouter


from apps.business.api.views import business,favorites
router = DefaultRouter()
router.register(r'businesses', business.BusinessViewSet, basename='business')
urlpatterns = [
    path("favorites/",favorites.FavoriteList.as_view()),
    path("categories/",business.CategoryList.as_view()),
    path("favorites/create/",favorites.FavoriteCreate.as_view()),
]

urlpatterns += router.urls
