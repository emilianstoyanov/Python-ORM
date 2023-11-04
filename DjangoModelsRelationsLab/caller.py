import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Subject, Student

# keep the data from the previous exercise, so you can reuse it

student1 = Student.objects.create(student_id="M1051", first_name="Alice",

                                  last_name="Johnson", birth_date="2000-01-15", email="a.johnson@abv.bg")

student2 = Student.objects.create(student_id="S217", first_name="Bob",

                                  last_name="Smith", birth_date="2001-05-20", email="bobby@gmail.com")

subject1 = Subject.objects.get(name="Mathematics")

subject2 = Subject.objects.get(name="History")

subject3 = Subject.objects.get(name="Physics")

student1.subjects.add(subject1, subject2)

student2.subjects.add(subject1, subject2, subject3)

math_subject = Subject.objects.get(name="Mathematics")

math_students = math_subject.student_set.all()

for student in math_students:
    print(f"{student.first_name} {student.last_name} is enrolled in Mathematics.")

history_subject = Subject.objects.get(name="History")

history_students = history_subject.student_set.all()

for student in history_students:

    print(f"{student.first_name} {student.last_name} is enrolled in History.")

physics_subject = Subject.objects.get(name="Physics")

physics_students = physics_subject.student_set.all()

for student in physics_students:
    print(f"{student.first_name} {student.last_name} is enrolled in Physics.")
