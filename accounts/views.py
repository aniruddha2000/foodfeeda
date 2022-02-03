from accounts.models import Donner
from accounts.serializers import DonnerRegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny


class DonnerRegisterView(CreateAPIView):
    queryset = Donner.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DonnerRegisterSerializer
