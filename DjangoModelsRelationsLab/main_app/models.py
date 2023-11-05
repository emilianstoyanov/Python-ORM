from django.db import models
from datetime import date


GRADES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('F', 'F'),
)

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


# Many-To-Many Relationship
class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField('Subject', through='StudentEnrollment')


class StudentEnrollment(models.Model):
    student = models.ForeignKey('Subject', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=date.today)
    grade = models.CharField(max_length=1, choices=GRADES)

    # class Meta:
    #     db_table = 'StudentEnrollment'
