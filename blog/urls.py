from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("otabek-abdiraimov-blog-admin-panel/", admin.site.urls),
    path("", include("posts.urls")),
]
