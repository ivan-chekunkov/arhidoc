from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    pub_create = models.DateTimeField(
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
        ordering = ["-pub_create"]

    def __str__(self):
        return self.name


class Doc(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование документа",
        help_text="Введите наименование документа",
    )
    pub_create = models.DateTimeField(
        verbose_name="Дата создания документа",
        auto_now_add=True,
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
        related_name="doc",
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ["-pub_create"]

    def __str__(self):
        return self.name[:10]
