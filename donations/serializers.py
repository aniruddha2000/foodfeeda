from rest_framework import serializers

from donations.models import Donner_paydetails


class OrderSerializer(serializers.ModelSerializer):

    order_date = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = Donner_paydetails
        fields = '__all__'
        depth = 2
