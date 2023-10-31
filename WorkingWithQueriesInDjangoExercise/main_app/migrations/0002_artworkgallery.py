# Generated by Django 4.2.6 on 2023-10-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtWorkGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('art_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
