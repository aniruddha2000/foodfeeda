import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.models import CustomUser


class VerifyEmail(GenericAPIView):
    def get(self, request):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms='HS256')
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response({"email": "Successfully verified"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({"error": "Activation Expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
