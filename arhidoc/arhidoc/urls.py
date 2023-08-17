from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("docbase.urls", namespace="docbase")),
    path("admin/", admin.site.urls),
]
