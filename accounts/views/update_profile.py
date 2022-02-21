from rest_framework.generics import (
    UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import Donner, NGO
from accounts.serializers import (
    DonnerUpdateUserSerializer, NGOUpdateUserSerializer)


class DonnerUpdateProfileView(UpdateAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Donner.objects.all()
    serializer_class = DonnerUpdateUserSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"data": serializer.data, "status": "Successfully updated Donner details"})


class NGOUpdateProfileView(UpdateAPIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = NGO.objects.all()
    serializer_class = NGOUpdateUserSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"data": serializer.data, "status": "Successfully updated NGO details"})
