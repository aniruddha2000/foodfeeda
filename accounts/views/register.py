from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import NGO, Donner
from accounts.serializers import (
    DonnerDetailSerializer, DonnerRegisterSerializer, NGODetailSerializer,
    NGORegisterSerializer,)
from accounts.utils import Util


class DonnerRegisterView(CreateAPIView):
    queryset = Donner.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonnerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            token = RefreshToken.for_user(user).access_token
            current_site = "localhost:3000"
            relative_link = reverse("email_verify")

            absurl = "http://" + current_site + \
                relative_link + "?token=" + str(token)
            email_body = "Hi " + user.first_name + \
                " use link below to verify your email\n" + absurl
            data = {
                "to_email": user.email,
                "email_subject": "Verify your email",
                "email_body": email_body,
            }
            Util.send_email(data)

            return Response(
                {
                    "user": DonnerDetailSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "status": "Successfully created donner account",
                }
            )
        else:
            return Response(
                {
                    "status": "couldn't create donner account",
                }
            )


class NGORegisterView(CreateAPIView):

    queryset = NGO.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = NGORegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            token = RefreshToken.for_user(user).access_token
            current_site = "localhost:3000"
            relative_link = reverse("email_verify")

            absurl = "http://" + current_site + \
                relative_link + "?token=" + str(token)
            email_body = "Hi " + user.name + \
                " use link below to verify your email\n" + absurl
            data = {
                "to_email": user.email,
                "email_subject": "Verify your email",
                "email_body": email_body,
            }
            Util.send_email(data)

            return Response(
                {
                    "user": NGODetailSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "status": "Successfully created ngo account",
                }
            )
        else:
            return Response(
                {
                    "status": "couldn't create ngo account",
                }
            )
