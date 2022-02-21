from rest_framework.generics import (
    UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import Donner, NGO
from accounts.serializers import (
    DonnerChangePasswordSerializer, NGOChangePasswordSerializer)


class DonnerChangePasswordView(UpdateAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Donner.objects.all()
    serializer_class = DonnerChangePasswordSerializer


class NGOChangePasswordView(UpdateAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = NGO.objects.all()
    serializer_class = NGOChangePasswordSerializer
