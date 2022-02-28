from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import (
    DjangoUnicodeDecodeError, smart_bytes, smart_str)
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import CustomUser
from accounts.serializers import (
    EmailResetPasswordSerializer, SetNewPasswordSerializer)
from accounts.utils import Util


class EmailResetPassword(GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = EmailResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = "localhost:3000"
            relative_link = reverse(
                "password-reset-confirm", kwargs={'uidb64': uidb64, 'token': token})

            absurl = "http://" + current_site + relative_link
            email_body = "Hello \n Use link below to reset your password\n" + absurl
            data = {
                "to_email": user.email,
                "email_subject": "Reset your password",
                "email_body": email_body,
            }
            Util.send_email(data)

        return Response(
            {"success": "We have sent you a link to reset your password"},
            status=HTTP_200_OK
        )


class PasswordTokenCheckAPI(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {"error": "Token is not valid, please request a new one"},
                    status=HTTP_401_UNAUTHORIZED
                )

            return Response(
                {
                    "success": True,
                    "messege": "Credential valid",
                    "uidb64": uidb64,
                    "token": token
                },
                status=HTTP_200_OK
            )

        except DjangoUnicodeDecodeError:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response(
                    {"error": "Token is not valid, please request a new one"},
                    status=HTTP_401_UNAUTHORIZED
                )


class SetNewPasswordAPIView(GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"success": True, "message": "Password reset success"}, status=HTTP_200_OK)
