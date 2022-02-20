from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from posts.models import DonationPost, FoodPost


class DonationPostAdmin(admin.ModelAdmin):
    model = DonationPost
    list_display = (
        "author",
        "campaignName",
        "post_date",
        "accepted",
    )
    list_filter = (
        "author",
        "campaignName",
        "accepted",
    )
    fieldsets = (
        ("Details", {"fields": ("author", "campaignName", "purpose", "amount")}),
        ("ID & Date", {"fields": ("id", "post_date")}),
        ("Status", {"fields": ("accepted",)}),
    )
    readonly_fields = (
        "id",
        "post_date",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "author",
                    "id",
                    "campaignName",
                    "purpose",
                    "amount",
                    "post_date",
                    "accepted",
                ),
            },
        ),
    )
    search_fields = ("author",)
    ordering = ("id",)


class FoodPostAdmin(admin.ModelAdmin):
    model = FoodPost
    list_display = (
        "auther",
        # "name",
        "created_at",
        "received",
    )
    list_filter = (
        "auther",
        # "name",
        "received",
    )
    fieldsets = (
        ("Details", {"fields": ("auther", "description", "food_photo")}),
        ("ID & Date", {"fields": ("id", "created_at")}),
        ("Location", {"fields": ("lat", "lon", "place")}),
        ("Status", {"fields": ("received",)}),
    )
    readonly_fields = (
        "id",
        "created_at",
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "auther",
                    "id",
                    # "food_post_id",
                    # "name",
                    "food_photo",
                    "description",
                    "lat",
                    "lon",
                    "place",
                    "received",
                    "created_at",
                ),
            },
        ),
    )
    search_fields = ("auther",)
    ordering = ("id",)


admin.site.register(DonationPost, DonationPostAdmin)
admin.site.register(FoodPost, FoodPostAdmin)
