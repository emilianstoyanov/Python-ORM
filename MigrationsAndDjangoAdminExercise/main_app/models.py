from django.db import models

class Shoe(models.Model):
    brand = models.CharField(
        max_length=25,
    )

    size = models.PositiveIntegerField()
