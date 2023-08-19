from django.apps import AppConfig


class DocbaseConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "docbase"
    verbose_name = "База данных для работы секретаря"
