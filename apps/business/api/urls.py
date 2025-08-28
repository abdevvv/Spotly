from django.urls import path
from rest_framework.routers import DefaultRouter


from apps.business.api.views import business,favorites,review
router = DefaultRouter()
router.register(r'businesses', business.BusinessViewSet, basename='business')
urlpatterns = [
    path("categories/",business.CategoryList.as_view()),

    path("favorites/",favorites.FavoriteList.as_view()),
    path("favorites/create/",favorites.FavoriteCreate.as_view()),
    
    path("reviews/<int:business_id>/", review.ReviewList.as_view(), name=""),
    path("reviews/create/", review.ReviewCreate.as_view(), name="")
]

urlpatterns += router.urls
