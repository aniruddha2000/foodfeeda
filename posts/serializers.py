
import os
from django.conf import settings
from rest_framework import serializers
from .models import FoodPost


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPost
        fields = [
            'title',
            'name',
            'food_photo',
            'description',
            'lat',
            'lon',
           
           
        ]

    def validate_title(self, value):
        if len(value) > 100:
            return serializers.ValidationError("Max title length is 100 characters")
        return value

    def validate_description(self, value):
        if len(value) > 200:
            return serializers.ValidationError(
                "Max description length is 200 characters"
            )
        return value
    
    def clean_image(self, value):
        initial_path = value.path
        new_path = settings.MEDIA_ROOT + value.name
        os.rename(initial_path, new_path)
        return value


class PostListSerializer(serializers.ModelSerializer):


    class Meta:
        model = FoodPost
        fields = [
            'title',
            'user',
            'id',
            'name',
            'food_photo',
            'description',
            'lat',
            'lon',
            'created_at',
        ]


