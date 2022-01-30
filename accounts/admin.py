from django.contrib import admin
from .models import CustomUser, NGO, Donner


admin.site.register(CustomUser)
admin.site.register(NGO)
admin.site.register(Donner)
