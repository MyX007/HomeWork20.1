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
                Category(**category['fields'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(**product['fields'])
            )

        Product.objects.bulk_create(product_for_create)
