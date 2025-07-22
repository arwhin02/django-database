import json
from django.core.management.base import BaseCommand
from testdb.models import Products 

class Command(BaseCommand):
    help = 'Import products from products.json'

    def handle(self, *args, **kwargs):
        with open('products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:
            Products.objects.update_or_create(
                id=item['id'],
                defaults={
                    'name': item['name'],
                    'price': item['price'],
                    'description': item['description'],
                    'stock': item['stock']
                }
            )

        self.stdout.write(self.style.SUCCESS('Products imported successfully.'))
