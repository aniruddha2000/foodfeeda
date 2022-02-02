from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from posts.models import DonationPost, FoodPost


class DonationPostAdmin(admin.ModelAdmin):
    model = DonationPost
    list_display = (
        "user",
        "campaignName",
        "post_date",
        "accepted",
    )
    list_filter = (
        "user",
        "campaignName",
        "accepted",
    )
    fieldsets = (
        ("Details", {"fields": ("user", "campaignName", "purpose", "amount")}),
        ("ID & Date", {"fields": ("donation_post_id", "post_date")}),
        ("Status", {"fields": ("accepted",)}),
    )
    readonly_fields = (
        "donation_post_id",
        "post_date",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user",
                    "donation_post_id",
                    "campaignName",
                    "purpose",
                    "amount",
                    "post_date",
                    "accepted",
                ),
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("donation_post_id",)


class FoodPostAdmin(admin.ModelAdmin):
    model = FoodPost
    list_display = (
        "user",
        "name",
        "created_at",
        "received",
    )
    list_filter = (
        "user",
        "name",
        "received",
    )
    fieldsets = (
        ("Details", {"fields": ("user", "name", "description", "food_photo")}),
        ("ID & Date", {"fields": ("food_post_id", "created_at")}),
        ("Location", {"fields": ("lat", "lon")}),
        ("Status", {"fields": ("received",)}),
    )
    readonly_fields = (
        "food_post_id",
        "created_at",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "user",
                    "food_post_id",
                    "name",
                    "food_photo",
                    "description",
                    "lat",
                    "lon",
                    "received",
                    "created_at",
                ),
            },
        ),
    )
    search_fields = ("user",)
    ordering = ("food_post_id",)


admin.site.register(DonationPost, DonationPostAdmin)
admin.site.register(FoodPost, FoodPostAdmin)
