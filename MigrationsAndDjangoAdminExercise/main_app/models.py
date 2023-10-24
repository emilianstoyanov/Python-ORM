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


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    age = models.PositiveIntegerField()

    grade = models.CharField(
        max_length=10,
    )

    date_of_birth = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Supplier(models.Model):
    name = models.CharField(
        max_length=100,
    )

    contact_person = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
    )

    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.phone}"


class Person(models.Model):
    name = models.CharField(
        max_length=40,
    )

    age = models.PositiveIntegerField()

    age_group = models.CharField(
        max_length=20,
        default='No age group',
    )

    def __str__(self):
        return f"Name: {self.name}"
