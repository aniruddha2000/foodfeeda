from accounts.models import Donner, NGO
from accounts.serializers import DonnerRegisterSerializer, NGORegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class DonnerRegisterView(CreateAPIView):
    queryset = Donner.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonnerRegisterSerializer


class NGORegisterView(CreateAPIView):
    queryset = NGO.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = NGORegisterSerializer
