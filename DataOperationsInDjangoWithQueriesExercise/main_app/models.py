from django.db import models


# Create your models here.


class Pet(models.Model):

    name = models.CharField(
        max_length=40,
    )

    species = models.CharField(
        max_length=40,
    )

