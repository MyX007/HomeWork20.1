# Generated by Django 5.0.7 on 2024-07-24 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_categoty',
            new_name='product_category',
        ),
    ]
