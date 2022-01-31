from django.contrib import admin
from posts.models import DonationPost, FoodPost

admin.site.register(FoodPost)
admin.site.register(DonationPost)
