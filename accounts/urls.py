from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import DonnerRegisterView

urlpatterns = [
    path("auth/login/", obtain_auth_token, name="create-token"),
    path("auth/donner/register/", DonnerRegisterView.as_view(), name="create-token"),
]
