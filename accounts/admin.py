from pyexpat import model
from django.contrib import admin
from .models import CustomUser, NGO, Donner, Address


class AddressInline(admin.StackedInline):
    model = Address


class UserAdmin(admin.ModelAdmin):
    inlines = (AddressInline,)


admin.site.register(NGO, UserAdmin)
admin.site.register(Donner, UserAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Address)
