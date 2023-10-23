from django.db import models


class Shoe(models.Model):
    brand = models.CharField(
        max_length=25,
    )

    size = models.PositiveIntegerField()


class UniqueBrands(models.Model):
    brand_name = models.CharField(
        max_length=25
    )


class EventRegistration(models.Model):
    event_name = models.CharField(
        max_length=60,
    )

    participant_name = models.CharField(
        max_length=50
    )

    registration_date = models.DateTimeField()

    def __str__(self):
        return f"{self.participant_name} - {self.event_name}"
