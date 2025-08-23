from django.urls import path


from apps.business.api.views import business
urlpatterns = [
    path('business/',business.BusinessList.as_view())
]
