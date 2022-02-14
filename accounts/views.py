from accounts.models import Donner, NGO
from accounts.serializers import (
    DonnerRegisterSerializer,
    NGORegisterSerializer,
    DonnerDetailSerializer,
    NGODetailSerializer,
    MyTokenObtainPairSerializer,
    DonnerChangePasswordSerializer,
    NGOChangePasswordSerializer,
    DonnerUpdateUserSerializer,
    NGOUpdateUserSerializer
)
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

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


class APILogoutView(APIView):

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"status": "OK, goodbye, all refresh tokens blacklisted"})
        refresh_token = self.request.data.get('refresh_token')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"status": "OK, goodbye"})


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
