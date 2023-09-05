from django.urls import path

from . import views

app_name = "docbase"
urlpatterns = [
    path("", views.index, name="main"),
    path("load/<path>/", views.download, name="load"),
    path("all_category", views.all_category, name="all_category"),
    path("docs_category/<pk>", views.docs_category, name="docs_category"),
    path("create_docs<pk>", views.create_docs, name="create_docs"),
    path("searche", views.searche, name="searche"),
]
