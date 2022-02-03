import datetime
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)

    phone_number = PhoneNumberField()

    country = CountryField(blank_label="(select country)")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class NGO(CustomUser):

    name = models.CharField(max_length=30)
    ngo_approval_cert = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "NGO"


GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]


class Donner(CustomUser):

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default=1)
    coins = models.IntegerField(default=5)
    DOB = models.DateField(_("DOB"), default=datetime.date.today)
    profile_photo = models.ImageField(upload_to="media/images", null=True, default="")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Donner"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
