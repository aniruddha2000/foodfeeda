from django.db import models
from accounts.models import Donner

# Create your models here.
class Donner_Post(models.Model):
    user = models.OneToOneField(Donner,on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    food_photo = models.ImageField(upload_to="media/images", null=True, default="")
    description = models.TextField(blank = True)
    lon=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat=models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    received=models.BooleanField(initial=False)
    created_at = models.DateTimeField(auto_now_add=True)