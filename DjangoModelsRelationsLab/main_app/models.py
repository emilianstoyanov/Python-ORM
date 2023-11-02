from django.db import models


# Create your models here

# one
class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# many
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    # One-To-Many Relationship
    lecturer = models.ForeignKey('Lecturer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"
