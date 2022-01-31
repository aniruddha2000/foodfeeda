from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db import models

from accounts.models import Donner, NGO


class Donner_Post(models.Model):
    user = models.OneToOneField(Donner, on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    food_photo = models.ImageField(upload_to="media/images", null=True, default="")
    description = models.TextField(blank=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    received = models.BooleanField(initial=False)
    created_at = models.DateTimeField(auto_now_add=True)


class DonationPost(models.Model):
    user = models.ForeignKey(NGO, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    campaignName = models.CharField(max_length=50)
    purpose = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    post_date = models.DateTimeField(auto_now=True, editable=False)
    donation_post_phone_number = models.CharField(max_length=10)
    accepted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.donation_post_phone_number = slugify(NGO.phone_number)
        oneNotAcceptedPostExist = False
        posts = DonationPost.objects.all()
        for post in posts:
            if post.accepted is False:
                oneNotAcceptedPostExist = True
                break

        if not self.pk and DonationPost.objects.exists() or oneNotAcceptedPostExist:
            raise ValidationError("Only one post allowed!")
        super(DonationPost, self).save(*args, **kwargs)
