from django.urls import path
from .views import (
    PostCreateAPIView,
    ListPostAPIView,

)

app_name = "posts"

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path("create/", PostCreateAPIView.as_view(), name="create_post"),


]