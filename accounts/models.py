import datetime
from enum import unique

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from setuptools import Require
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class Address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    country = CountryField(blank_label="(select country)")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} {self.country} {self.state}"

    class Meta:
        verbose_name = "Address"


class NGO(CustomUser):
    # TODO: Location, Contact
    phone_number = PhoneNumberField()
    address_ngo = models.OneToOneField(Address, on_delete=models.CASCADE)
    ngo_approval_cert = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "NGO"
        unique_together = ("phone_number",)


GENDER_CHOICES = [("Male", "Male"), ("Female", "Female"), ("Others", "Others")]


class Donner(CustomUser):
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default=1)
    address_donner = models.OneToOneField(Address, on_delete=models.CASCADE)
    coins = models.IntegerField(default=5)
    DOB = models.DateField(_("DOB"), default=datetime.date.today)
    profile_photo = models.ImageField(upload_to="media/images", null=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Donner"
        unique_together = ("phone_number",)
