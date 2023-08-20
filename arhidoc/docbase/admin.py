from django.contrib import admin

from .models import Category, Doc


class DocAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "pub_create",
        "number",
        "category",
    )
    search_fields = ("name",)
    list_filter = ("pub_create",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "pub_create",
        "counter",
    )
    search_fields = ("name",)
    list_filter = ("pub_create",)
    empty_value_display = "-пусто-"


admin.site.register(Doc, DocAdmin)
admin.site.register(Category, CategoryAdmin)
