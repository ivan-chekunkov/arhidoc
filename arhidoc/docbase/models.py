from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    date_created = models.DateTimeField(
        verbose_name="Дата создания категории",
        auto_now_add=True,
    )
    counter = models.IntegerField(
        verbose_name="Индекс для нового документа",
        default=1,
        help_text="Введите номер для нового элемента данной категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name


class Doc(models.Model):
    date_created = models.DateTimeField(
        verbose_name="Дата создания документа",
        auto_now_add=True,
    )
    data_doc = models.DateTimeField(
        verbose_name="Дата документа",
        help_text="Введите дату документа",
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование документа",
        help_text="Введите наименование документа",
    )
    number = models.CharField(
        max_length=10,
        verbose_name="Номер документа",
        help_text="Введите номер документа",
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="docs",
    )
    file_doc = models.FileField(
        upload_to="documents/",
        verbose_name="Путь до файла документа",
        help_text="Укажите путь до файла документа",
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ["-date_created"]

    def __str__(self):
        return self.name[:10]
