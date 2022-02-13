from django.urls import path
from .views import (
    PostCreateAPIView,PostUpdateDeleteAPIView,AllPostListRetrieveAPIView,DonationPostCreateAPIView,
    DonationPostUpdateAPIView,DonationAllPostListRetrieveAPIView,

)

app_name = "posts"

urlpatterns = [

    path("foodpost/", PostCreateAPIView.as_view(), name="create_view_post"),
    path("foodpost/<int:id>/", PostUpdateDeleteAPIView.as_view(), name="up_del_post"),
    path("foodpost/search/<str:place>/", AllPostListRetrieveAPIView.as_view(), name="search_post"),
    path("donationpost/",DonationPostCreateAPIView.as_view(), name="create_view_donationpost"),
    path("donationpost/<int:id>/", DonationPostUpdateAPIView.as_view(), name="donation_up_del_post"),
    path("donationpost/list/", DonationAllPostListRetrieveAPIView.as_view(), name="donation_postlist"),
 
]