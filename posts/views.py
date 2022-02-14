
from django.http import JsonResponse

from accounts.models import NGO, Donner
from rest_framework import status
from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import FoodPost
from posts.pagination import PostLimitOffsetPagination
from posts.serializers import *


class PostCreateAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = FoodPost.objects.all()
    serializer_class = PostCreateSerializer
    pagination_class = PostLimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(auther=Donner.objects.get(id=self.request.user.id))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PostListSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = FoodPost.objects.filter(
            auther=Donner.objects.get(id=self.request.user.id))
        return queryset


class PostUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = FoodPost.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PostListSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer = PostListSerializer(instance=instance, many=False)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AllPostListRetrieveAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = FoodPost.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self):
        place = self.kwargs['place']
        return FoodPost.objects.filter(place=place)


class DonationPostCreateAPIView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = DonationPost.objects.all()
    serializer_class = DonationPostCreateSerializer
    pagination_class = PostLimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=NGO.objects.get(id=self.request.user.id))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = DonationPostListSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = DonationPostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = DonationPost.objects.filter(
            author=NGO.objects.get(id=self.request.user.id))
        return queryset


class DonationPostUpdateAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = DonationPost.objects.all()
    serializer_class = DonationPostCreateSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DonationPostListSerializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer = DonationPostListSerializer(instance=instance, many=False)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()


class DonationAllPostListRetrieveAPIView(ListAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    authentication_classes = (JWTAuthentication,)

    queryset = DonationPost.objects.filter(accepted=True)
    serializer_class = DonationPostListSerializer
    pagination_class = PostLimitOffsetPagination
