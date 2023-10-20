from django.db import models


# Create your models here.


class MyBook(models.Model):
    name = models.TextField(
        max_length=49,
        unique=True,
    )
