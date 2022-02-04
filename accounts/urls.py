from django.urls import path
from accounts.views import (
    DonnerRegisterView,
    NGORegisterView,
    DonnerViewSet,
    NGOViewSet,
    MyObtainTokenPairView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path(
        "auth/login/token/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/login/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/donner/register/", DonnerRegisterView.as_view(), name="create-donner"),
    path("auth/ngo/register/", NGORegisterView.as_view(), name="create-ngo"),
    path("donner/user/<id>", DonnerViewSet.as_view(), name="donner-user"),
    path("ngo/user/<id>", NGOViewSet.as_view(), name="ngo-user"),
]
