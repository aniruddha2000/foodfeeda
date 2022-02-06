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
from rest_framework.response import Response

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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
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
