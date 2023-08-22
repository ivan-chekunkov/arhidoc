from django.urls import path

from . import views

app_name = "docbase"
urlpatterns = [
    path("", views.index, name="main"),
    path("load/", views.download, name="load"),
]
