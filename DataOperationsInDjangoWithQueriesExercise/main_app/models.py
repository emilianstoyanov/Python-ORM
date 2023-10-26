from django.db import models


# Create your models here.


class Pet(models.Model):
    name = models.CharField(
        max_length=40,
    )

    species = models.CharField(
        max_length=40,
    )

    def __str__(self):
        return f"{self.name} is a very cute {self.species}!"


class Artifact(models.Model):
    name = models.CharField(
        max_length=70,
    )

    origin = models.CharField(
        max_length=70,
    )

    age = models.PositiveIntegerField()

    description = models.TextField()

    is_magical = models.BooleanField(
        default=False,
    )


class Location(models.Model):
    name = models.CharField(
        max_length=100,
    )

    region = models.CharField(
        max_length=50,
    )

    population = models.PositiveIntegerField()

    description = models.TextField()

    is_capital = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name
