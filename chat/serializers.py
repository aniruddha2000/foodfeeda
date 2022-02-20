from rest_framework.serializers import ModelSerializer, SlugRelatedField

from accounts.models import CustomUser
from chat.models import Message


class MessageSerializer(ModelSerializer):
    sender = SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all())
    receiver = SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class MessageSerializerForReceiver(ModelSerializer):
    receiver = SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
