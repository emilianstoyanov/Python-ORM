import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Pet, Artifact, Location
from automatic_recording_db import populate_model_with_data


def create_pet(name: str, species: str) -> str:
    Pet.objects.create(
        name=name,
        species=species,
    )
    return f"{name} is a very cute {species}!"

    # Pet.objects.all().delete()


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts() -> None:
    Pet.objects.all().delete()


# delete_all_artifacts()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))


def show_all_locations():
    locations = Location.objects.all().order_by('-id')
    return '\n'.join(str(x) for x in locations)


# print(show_all_locations())


def new_capital() -> None:
    Location.objects.filter(pk=1).update(is_capital=True)
    # location = Location.objects.first()
    # location.is_capital = True
    # location.save()

new_capital()
def get_capitals():
    return Location.objects.all()


def delete_first_location():
    Location.objects.all().delete()

# show_all_locations()
# new_capital()
# show_all_locations()

# print(new_capital())
# print(get_capitals())
# delete_first_location()


# populate_model_with_data(Location, 10)
