from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('razorpay/', include("donations.urls")),
    path("api/", include("accounts.urls")),
    path('post/',include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
