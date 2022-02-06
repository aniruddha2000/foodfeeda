from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,

)
from rest_framework import status
from accounts.models import Donner
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,

)

from .pagination import PostLimitOffsetPagination
from .models import FoodPost
from .serializers import *

# Create your views here.
class PostCreateAPIView(CreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = FoodPost.objects.all()
    serializer_class = PostCreateSerializer
    def perform_create(self,serializer):
        return serializer.save(Donner.objects.get(user=self.request.user))
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance=self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer=PostListSerializer(instance=instance,many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)    
    def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)   

class ListPostAPIView(ListAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = FoodPost.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostLimitOffsetPagination

