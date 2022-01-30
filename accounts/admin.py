from django.contrib import admin
from .models import CustomUser, NGO


# from .models import NGO,Donner
# # Register your models here.
# admin.site.register(Donner)
admin.site.register(NGO)
admin.site.register(CustomUser)
