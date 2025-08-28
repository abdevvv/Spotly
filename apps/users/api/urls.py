from django.urls import path
from apps.users.api.views import authentication,accounts
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    #auth
    path("register/", authentication.RegiserGeneric.as_view(), name=""),
    path('login/',authentication.LoginGeneric.as_view()),
    path("refresh/", TokenRefreshView.as_view()),

    #accounts
    path("user/", accounts.UserGeneric.as_view(), name="")
]
