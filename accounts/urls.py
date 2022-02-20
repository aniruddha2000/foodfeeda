from django.urls import path
from accounts.views import (
    DonnerRegisterView,
    NGORegisterView,
    DonnerViewSet,
    NGOViewSet,
    MyObtainTokenPairView,
    APILogoutView,
    DonnerChangePasswordView,
    NGOChangePasswordView,
    DonnerUpdateProfileView,
    NGOUpdateProfileView,
    DonnerVerifyEmail,
    NGOVerifyEmail
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path(
        "auth/login/token/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/login/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/login/token/verify/",
         TokenVerifyView.as_view(), name="token_verify"),
    path("auth/logout/", APILogoutView.as_view(), name="logout"),
    path("auth/donner/register/", DonnerRegisterView.as_view(), name="create-donner"),
    path("auth/ngo/register/", NGORegisterView.as_view(), name="create-ngo"),
    path("auth/donner/change-password/<int:pk>/",
         DonnerChangePasswordView.as_view(), name="change-password-donner"),
    path("auth/ngo/change-password/<int:pk>/",
         NGOChangePasswordView.as_view(), name="change-password-ngo"),
    path("donner/update-profile/<int:pk>/",
         DonnerUpdateProfileView.as_view(), name="update-profile-donner"),
    path("ngo/update-profile/<int:pk>/",
         NGOUpdateProfileView.as_view(), name="update-profile-ngo"),
    path("donner/user/<id>", DonnerViewSet.as_view(), name="donner-user"),
    path("ngo/user/<id>", NGOViewSet.as_view(), name="ngo-user"),
    path("auth/donner/email-veryfy/", DonnerVerifyEmail.as_view(), name="email_verify_donner"),
    path("auth/ngo/email-veryfy/", NGOVerifyEmail.as_view(), name="email_verify_ngo"),
]
