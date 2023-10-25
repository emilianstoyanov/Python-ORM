import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student

# Import your models
# Create and check models
# Run and print your queries

# print(Student.objects.get(student_id='1'))
# print(type(Student.objects.all()))

all_students = [['FC5205', 'John', 'Doje', '1996-05-10', 'johhn.doe@university.com'],
                ['FC5206', 'John', 'Doge', '1945-05-10', 'jyohn.doe@university.com']
                ]


def add_students():
    for student in all_students:
        new_employee = Student(student_id=student[0],
                               first_name=student[1],
                               last_name=student[2],
                               birth_date=student[3],
                               email=student[4],
                               )
        new_employee.save()

        # or
    # Student.objects.create(
    #     student_id='FC5205',
    #     first_name='John',
    #     last_name='Doje',
    #     birth_date='1996-05-10',
    #     email='johhn.doe@university.com',
    # )


add_students()
