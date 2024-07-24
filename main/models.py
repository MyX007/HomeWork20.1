from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    category_description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f''

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название')
    product_description = models.CharField(max_length=150, verbose_name='Описание')
    product_img = models.ImageField(upload_to='products_img/', verbose_name='Фото', **NULLABLE)
    product_categoty = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Категория')
    product_price = models.IntegerField(verbose_name="Цена", **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Дата создания")
    updated_at = models.DateTimeField(verbose_name="Дата последнего изменения")

    def __str__(self):
        return f""

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
