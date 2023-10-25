import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student

# Import your models
# Create and check models
# Run and print your queries

print(Student.objects.get(student_id='1'))

# print(type(Student.objects.all()))
