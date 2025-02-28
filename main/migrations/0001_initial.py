# Generated by Django 5.0.7 on 2024-07-24 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Категория')),
                ('category_description', models.CharField(max_length=150, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Название')),
                ('product_description', models.CharField(max_length=150, verbose_name='Описание')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='products_img/', verbose_name='Фото')),
                ('product_price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(verbose_name='Дата последнего изменения')),
                ('product_categoty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Категория', to='main.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
