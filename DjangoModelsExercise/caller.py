import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoorm.settings")
django.setup()

# Set up Django
from django.core.exceptions import ValidationError
from tasks.models import CustomPerson
try:
    invalid_person = CustomPerson(
        name="Emilian",
        age=150,
    )

    invalid_person.full_clean()

except ValidationError as e:
    print(e)
