from django.urls import path

from . import views

app_name = "docbase"
urlpatterns = [
    path("", views.index, name="main"),
    path("load/", views.download, name="load"),
    path("model-form-upload", views.model_form_upload, name="model_form_upload"),
    path("category", views.category, name="category")
]
