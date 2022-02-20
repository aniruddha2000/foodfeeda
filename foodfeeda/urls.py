from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('razorpay/', include("donations.urls")),
    path("api/", include("accounts.urls")),
    path('api/post/', include("posts.urls")),
    path('api/chat/', include("chat.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
