from rest_framework.serializers import ModelSerializer, SlugRelatedField
from chat.models import Message
from accounts.models import CustomUser


class MessageSerializer(ModelSerializer):
    sender = SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all())
    receiver = SlugRelatedField(
        many=False, slug_field='id', queryset=CustomUser.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
