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


# for _student in STUDENTS:
#     Student.objects.create(**_student)
#     print(Student.objects.create(**_student))

# print(Student.objects.all())


def get_students_info():
    students = Student.objects.all()
    students_info = []
    for student in students:
        students_info.append(
            f"Student №{student.student_id}: "
            f"{student.first_name} {student.last_name}; "
            f"Email: {student.email}"
        )
    return "\n".join(students_info)


def update_students_emails():
    for student in Student.objects.all():
        new_email = student.email.replace('abv.bg', 'uni-students.com')
        student.email = new_email
        student.save()
        print(student.email)


# update_students_emails()

def truncate_students():
    Student.objects.all().delete()


# truncate_students()
print(Student.objects.all())
print(f"Number of students: {Student.objects.count()}")
