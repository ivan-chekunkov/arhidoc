from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from docbase.views import model_form_upload

urlpatterns = [
    path("", include("docbase.urls", namespace="docbase")),
    path("admin/", admin.site.urls),
    re_path(r'^uploads/form/$', model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
