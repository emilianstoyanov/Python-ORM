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

STUDENTS = [
    {
        'student_id': '11111',
        'first_name': 'Emili',
        'last_name': 'Emili',
        'birth_date': '1945-05-10',
        'email': 'jyohgn.doe@univesity.co',

    },
    {
        'student_id': '22222',
        'first_name': 'Emii',
        'last_name': 'Emii',
        'birth_date': '1945-05-10',
        'email': 'jyffn.doe@univerity.co',

    },
]
for _student in STUDENTS:
    Student.objects.create(**_student)
    print(Student.objects.create(**_student))

print(Student.objects.all())