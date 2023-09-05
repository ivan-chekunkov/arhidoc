from django.contrib import admin

from .models import Category, Doc


class DocAdmin(admin.ModelAdmin):
    list_display = (
        "data_doc",
        "name",
        "number",
        "category",
        "date_created",
        "file_doc",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "date_created",
        "counter",
    )
    search_fields = ("name",)
    list_filter = ("date_created",)
    empty_value_display = "-пусто-"


admin.site.register(Doc, DocAdmin)
admin.site.register(Category, CategoryAdmin)
