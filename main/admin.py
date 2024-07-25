from django.contrib import admin
from main.models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_category', 'product_price')
    list_filter = ('product_category', 'product_name')
    search_fields = ('product_name', 'product_description')


