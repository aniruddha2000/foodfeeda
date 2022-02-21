from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
