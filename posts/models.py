from __future__ import unicode_literals
from accounts.models import Donner, NGO
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
# Create your models here.
class FoodPost(models.Model):
    user = models.ForeignKey(Donner, on_delete=models.CASCADE)
    food_post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    name = models.CharField(max_length=50)
    food_photo = models.ImageField(upload_to="media/images", null=True, default="")
    description = models.TextField(blank=True, max_length=500)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    received = models.BooleanField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def get_api_url(self):
        try:
            return reverse("posts_api:post_detail", kwargs={"slug": self.slug})
        except:
            None



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = FoodPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=FoodPost)



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
