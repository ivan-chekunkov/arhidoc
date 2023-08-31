# Generated by Django 2.2.9 on 2023-08-30 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование категории', max_length=100, verbose_name='Наименование категории')),
                ('pub_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания категории')),
                ('counter', models.IntegerField(default=1, help_text='Введите номер для нового элемента данной категории', verbose_name='Индекс для нового документа')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-pub_create'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание документа')),
                ('document', models.FileField(upload_to='documents/', verbose_name='Путь до документа')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки документа')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания документа')),
                ('data_doc', models.DateTimeField(null=True, verbose_name='Дата документа')),
                ('name', models.CharField(help_text='Введите наименование документа', max_length=100, verbose_name='Наименование документа')),
                ('number', models.CharField(help_text='Введите номер документа', max_length=10, verbose_name='Номер документа')),
                ('file_path', models.CharField(help_text='Укажите путь до файла документа', max_length=200, null=True, verbose_name='Путь до файла документа')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to='docbase.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['-pub_create'],
            },
        ),
    ]
