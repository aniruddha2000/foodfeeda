from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

from accounts.models import NGO, Donner


class FoodPost(models.Model):
    id = models.AutoField(primary_key=True)
    auther = models.ForeignKey(
        Donner, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=50)
    food_photo = models.ImageField(
        upload_to="media/images", null=True, default="")
    description = models.TextField(blank=True, max_length=180)
    lat = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(
        max_digits=22, decimal_places=16, blank=True, null=True)
    place = models.CharField(max_length=100,  default="")
    received = models.BooleanField(null=True, default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class DonationPost(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(NGO, on_delete=models.CASCADE)
    campaignName = models.CharField(max_length=50)
    purpose = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    post_date = models.DateTimeField(auto_now=True, editable=False)
    accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.campaignName
