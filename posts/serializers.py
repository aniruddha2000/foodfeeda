
import os
from django.conf import settings
from rest_framework import serializers
from .models import FoodPost,DonationPost


class PostCreateSerializer(serializers.ModelSerializer):
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






class PostListSerializer(serializers.ModelSerializer):


    class Meta:
        model = FoodPost
        fields = "__all__"
       
class DonationPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationPost
        fields = [
            'author',
            'campaignName',
            'purpose',
            'amount',

            
              
        ]
        read_only_fields = ['author']






class DonationPostListSerializer(serializers.ModelSerializer):


    class Meta:
        model = DonationPost
        fields = "__all__"
       


