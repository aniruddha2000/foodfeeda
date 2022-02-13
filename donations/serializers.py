from rest_framework import serializers

from donations.models import DonnerPayDetails


class OrderSerializer(serializers.ModelSerializer):

    order_date = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = DonnerPayDetails
        fields = '__all__'
        depth = 2
