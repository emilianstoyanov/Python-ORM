from django.db import models


# Create your models here.


class MyBook(models.Model):
    AUTH_CHOICES = (
        ('Stephen King', 'Stephen King'),
        ('Dan Brown', 'Dan Brown'),
        ('James Patterson', 'James Patterson'),
        ('Leo Tolstoy', 'Leo Tolstoy'),
        ('John Grisham', 'John Grisham'),
    )

    fist_name = models.CharField(
        max_length=10,
        unique=True,
        default='Ivan',
    )

    last_name = models.CharField(
        max_length=10,
        unique=True,
        default='Ivanov',

    )

    auth = models.TextField(
        max_length=30,
        unique=True,
        default='Stephen King',
    )

    genre = models.CharField(
        max_length=40,
        choices=AUTH_CHOICES,
        default='Stephen King',

    )

    def __str__(self):
        return self.auth
