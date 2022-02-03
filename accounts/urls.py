from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import DonnerRegisterView, NGORegisterView

urlpatterns = [
    path("auth/login/", obtain_auth_token, name="create-token"),
    path("auth/donner/register/", DonnerRegisterView.as_view(), name="create-donner"),
    path("auth/ngo/register/", NGORegisterView.as_view(), name="create-ngo"),
]
