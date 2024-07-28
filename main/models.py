from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')
    img = models.ImageField(upload_to='products_img/', verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Категория')
    price = models.IntegerField(verbose_name="Цена", **NULLABLE)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    updated_at = models.DateTimeField(verbose_name="Дата последнего изменения", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
