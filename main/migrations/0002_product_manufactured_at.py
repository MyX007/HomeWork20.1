# Generated by Django 5.0.7 on 2024-07-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата производства'),
        ),
    ]
