import json

from main.models import Category, Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('main_data.json', "r", encoding="UTF-8") as file:
            json_categories = json.load(file)
            categories = []
            for category in json_categories:
                if category['model'] == 'main.category':
                    categories.append(category)
            return categories

    @staticmethod
    def json_read_products():
        with open('main_data.json', "r", encoding="UTF-8") as file:
            json_products = json.load(file)
            products = []
            for product in json_products:
                if product['model'] == 'main.product':
                    products.append(product)
            return products

    def handle(self, *args, **options):

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(category_name=category['fields']['category_name'], category_description=category['fields']['category_description'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(product_name=product['fields']['product_name'],
                        product_description=product['fields']['product_description'],
                        product_category=Category.objects.get(pk=product['fields']['product_category']),
                        product_img=product['fields']['product_img'],
                        product_price=product['fields']['product_price'], created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'], manufactured_at=product['fields']['manufactured_at'])
            )

        Product.objects.bulk_create(product_for_create)
