from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from accounts.views.logout import APILogoutView
from accounts.views.password_change import (
    DonnerChangePasswordView, NGOChangePasswordView)
from accounts.views.password_change_email import (
    EmailResetPassword, PasswordTokenCheckAPI, SetNewPasswordAPIView)
from accounts.views.register import DonnerRegisterView, NGORegisterView
from accounts.views.token_obtain import MyObtainTokenPairView
from accounts.views.update_profile import (
    DonnerUpdateProfileView, NGOUpdateProfileView)
from accounts.views.user_view import DonnerViewSet, NGOViewSet
from accounts.views.verify_email import VerifyEmail

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
    path("auth/user/email-veryfy/", VerifyEmail.as_view(), name="email_verify"),
    path("auth/user/email/request-reset/",
         EmailResetPassword.as_view(), name="request-email-reset"),
    path("auth/user/email/password-reset/<uidb64>/<token>/",
         PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path("auth/user/email/password-reset-complete/",
         SetNewPasswordAPIView.as_view(), name="password-reset-complete"),
]
