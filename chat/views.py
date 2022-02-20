from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (
    authentication_classes, permission_classes)
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import NGO, Donner
from chat.models import Message
from chat.serializers import MessageSerializer, MessageSerializerForReceiver


class MessegeList(ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = MessageSerializer

    def get_queryset(self):
        sender = self.kwargs['sender']
        receiver = self.kwargs['receiver']

        queryset = Message.objects.filter(
            sender_id=sender, receiver_id=receiver)
        return queryset


class MessageListByReceiver(ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = MessageSerializerForReceiver

    def get_queryset(self):
        # sender = self.kwargs['sender']
        receiver = self.kwargs['receiver']

        queryset = Message.objects.filter(receiver_id=receiver)
        return queryset
