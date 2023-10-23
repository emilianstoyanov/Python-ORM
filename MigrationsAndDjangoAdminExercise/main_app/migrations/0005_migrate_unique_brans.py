# Generated by Django 4.2.4 on 2023-10-23 15:55
# python .\manage.py makemigrations main_app --name migrate_unique_brans --empty
from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    unique_brands_names = shoe.objects.values_list('brand', flat=True).distinct()

    unique_brands_to_create = [unique_brands(brand_name=brand_name) for brand_name in unique_brands_names]

    unique_brands.objects.bulk_create(unique_brands_to_create)

    # for brand_name in unique_brands_names:
    #     unique_brands.create(brand_name=brand_name)


def delete_unique_brands(apps, schema_editor):
    unique_brands = apps.get_model('main_app', 'UniqueBrands')
    unique_brands.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0004_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]
