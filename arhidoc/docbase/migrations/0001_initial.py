# Generated by Django 4.2.4 on 2023-09-05 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование категории",
                        max_length=100,
                        verbose_name="Наименование категории",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата создания категории",
                    ),
                ),
                (
                    "counter",
                    models.IntegerField(
                        default=1,
                        help_text="Введите номер для нового элемента данной категории",
                        verbose_name="Индекс для нового документа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["-date_created"],
            },
        ),
        migrations.CreateModel(
            name="Doc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата создания документа",
                    ),
                ),
                (
                    "data_doc",
                    models.DateTimeField(
                        help_text="Введите дату документа",
                        null=True,
                        verbose_name="Дата документа",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование документа",
                        max_length=100,
                        verbose_name="Наименование документа",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        help_text="Введите номер документа",
                        max_length=10,
                        verbose_name="Номер документа",
                    ),
                ),
                (
                    "file_doc",
                    models.FileField(
                        help_text="Укажите путь до файла документа",
                        upload_to="documents/",
                        verbose_name="Путь до файла документа",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="docs",
                        to="docbase.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Документ",
                "verbose_name_plural": "Документы",
                "ordering": ["-date_created"],
            },
        ),
    ]
