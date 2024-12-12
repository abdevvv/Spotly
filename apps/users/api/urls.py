from django.urls import path
from apps.users.api.views import authentication,resetpassword,accounts
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    #auth
    path("register/", authentication.RegiserGeneric.as_view(), name=""),
    path('login/',authentication.LoginGeneric.as_view()),
    path("refresh/", TokenRefreshView.as_view()),

    #reset_password
    path('email_request/',resetpassword.EmailRequestGeneric.as_view()),
    path('check_otp/',resetpassword.check_otp),
    path('reset_password/',resetpassword.ResetPasswordGeneric.as_view()),

    #accounts
    path("user/", accounts.UserGeneric.as_view(), name="")
]
