# Generated by Django 4.2.4 on 2023-10-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=25)),
            ],
        ),
    ]