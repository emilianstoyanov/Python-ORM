import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.core.management.base import BaseCommand
import random
import string
from main_app.models import Product


def handle(self, *args, **options):
    products = Product.objects.all()

    for product in products:
        print(product)
        # Generate a random number with a length of 10
        random_number = ''.join(random.choice(string.digits) for _ in range(10))
        print(random_number)

        # Save the random number to the product's random_number field
        product.random_number = random_number
        product.save()

        self.stdout.write(self.style.SUCCESS(f'Random number generated and saved for product {product.id}'))
