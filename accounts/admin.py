from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.models import NGO, Donner

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm


class DonnerAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Donner
    list_display = (
        "email",
        "first_name",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                    "coins",
                    "DOB",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "phone_number",
                    "country",
                    "state",
                    "city",
                    "pin",
                    "profile_photo",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class NGOAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = NGO
    list_display = (
        "email",
        "name",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "phone_number",
                    "country",
                    "state",
                    "city",
                    "pin",
                    "ngo_approval_cert",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(NGO, NGOAdmin)
admin.site.register(Donner, DonnerAdmin)
