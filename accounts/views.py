from accounts.models import Donner, NGO
from accounts.serializers import (
    DonnerRegisterSerializer,
    NGORegisterSerializer,
    DonnerDetailSerializer,
    NGODetailSerializer,
    MyTokenObtainPairSerializer,
)
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


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


class DonnerRegisterView(CreateAPIView):
    queryset = Donner.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonnerRegisterSerializer


class NGORegisterView(CreateAPIView):
    queryset = NGO.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = NGORegisterSerializer
