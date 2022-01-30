from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
import datetime 
from django.utils.timezone import now

from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=100)

    ## TODO: Location, contact

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


class NGO(CustomUser):
    # TODO: Location, Contact
    phone_number = PhoneNumberField()
    ngo_approval_cert = models.FileField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "NGO"

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
]
class Donner(CustomUser):
    # TODO: Location, Contact
    
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    country = CountryField(blank_label='(select country)')
    description=models.TextField(max_length=200,blank=False)
    date = models.DateField(_("Date"), default=datetime.date.today)
    time=models. DateTimeField(default=now ,null=True,blank=True)
    DOB=models.DateField(_("Date"), default=datetime.date.today)
    gender =models.CharField(max_length=100,choices=GENDER_CHOICES,default=1)
    city=models.CharField(max_length=100)
    state= models.CharField(max_length=50)
    pin=models.PositiveIntegerField()
    images=models.ImageField(upload_to='media/images',null=True,default='')
    coins = models.IntegerField(default=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Donner"
