from rest_framework.generics import (
    RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import Donner, NGO
from accounts.serializers import (
    DonnerDetailSerializer, NGODetailSerializer)


class DonnerViewSet(RetrieveAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = DonnerDetailSerializer
    queryset = Donner.objects.all()
    lookup_field = "id"


class NGOViewSet(RetrieveAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = NGODetailSerializer
    queryset = NGO.objects.all()
    lookup_field = "id"
