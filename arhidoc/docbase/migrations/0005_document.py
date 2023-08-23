# Generated by Django 4.2.4 on 2023-08-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("docbase", "0004_alter_category_options_doc_data_doc_doc_file_path"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("description", models.CharField(blank=True, max_length=255)),
                ("document", models.FileField(upload_to="documents/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]