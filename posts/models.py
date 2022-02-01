from django.core.exceptions import ValidationError
from django.db import models

from accounts.models import Donner, NGO


class FoodPost(models.Model):
    user = models.ForeignKey(Donner, on_delete=models.CASCADE)
    food_post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    food_photo = models.ImageField(upload_to="media/images", null=True, default="")
    description = models.TextField(blank=True, max_length=500)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    received = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class DonationPost(models.Model):
    user = models.ForeignKey(NGO, on_delete=models.CASCADE)
    donation_post_id = models.AutoField(primary_key=True)
    campaignName = models.CharField(max_length=50)
    purpose = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    post_date = models.DateTimeField(auto_now=True, editable=False)
    accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.campaignName
