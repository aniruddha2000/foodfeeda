from django.conf import settings
from rest_framework.serializers import ModelSerializer
from posts.models import FoodPost, DonationPost


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = FoodPost
        fields = [
            'auther',
            'title',
            'food_photo',
            'description',
            'lat',
            'lon',
            'place',
        ]
        read_only_fields = ['auther']


class PostListSerializer(ModelSerializer):

    class Meta:
        model = FoodPost
        fields = "__all__"


class DonationPostCreateSerializer(ModelSerializer):

    class Meta:
        model = DonationPost
        fields = [
            'author',
            'campaignName',
            'purpose',
            'amount',
        ]
        read_only_fields = ['author']


class DonationPostListSerializer(ModelSerializer):

    class Meta:
        model = DonationPost
        fields = "__all__"
