# Generated by Django 4.2.6 on 2023-10-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20231022_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.IntegerField(default=0),
        ),
    ]