import os
from typing import List

import django

from automatic_recording_db import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtWorkGallery, Laptop, ChessPlayer, Dungeon, Workout
from django.db.models import Case, When, Value, F, QuerySet


def show_highest_rated_art() -> str:
    best_artwork = ArtWorkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_artwork.art_name} is the highest-rated art with {best_artwork.rating} rating!"


def bulk_create_arts(first_art, second_art) -> None:
    ArtWorkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts() -> None:
    ArtWorkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    best_laptop = Laptop.objects.order_by('-price', 'id').first()

    return f"{best_laptop.brand} is the most expensive laptop available for {best_laptop.price}$!"


def bulk_create_laptops(*args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    # Laptop.objects.filter(Q(brand='Lenovo') | Q(brand='Asus')).update(storage=512)
    Laptop.objects.filter(brand_in=['Lenovo', 'Asus']).update(storage=512)


def update_to_16_GB_storage() -> None:
    Laptop.objects.filter(brand_in=['Apple', 'Dell', 'Acer']).update(storage=16)


def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand=['Asus'], then=Value('Windows')),
            When(brand=['Apple'], then=Value('MacOS')),
            When(brand=['Dell', 'Acer'], then=Value('Linux')),
            When(brand=['Lenovo'], then=Value('Chrome OS')),
            default=F('operation_system')
        )
    )

    # Laptop.objects.filter(brand=['Asus']).update(operation_system='Windows')
    # Laptop.objects.filter(brand=['Apple']).update(operation_system='MacOS')
    # Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')
    # Laptop.objects.filter(brand=['Lenovo']).update(operation_system='Chrome OS')


def delete_inexpencive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(*args) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(title='no title').delete()


# changes the games won for the players with a "GM" title to 30.
def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title='GM').update(games_won=30)


# changes the games lost for the players with "no title" to 2
def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)


# changes the games drawn for every player to 10.
def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


# changes the title to "GM" for every player with a rating greater than or equal to 2400.
def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


# changes the title to "IM" for every player with a rating between 2399 and 2300 (both inclusive).
def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


# changes the title to "FM" for every player with a rating between 2299 and 2200 (both inclusive).
def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")


def set_new_chefs() -> None:
    ChessPlayer.objects.update(
        chef=Case(
            When(type=['Breakfast'], then=Value('Gordon Ramsa')),
            When(type=['Lunch'], then=Value('Julia Chil')),
            When(type=['Dinner'], then=Value('Jamie Olive')),
            When(type=['Snack'], then=Value('Thomas Keller')),
            default=F('chef'),
        )
    )


def set_new_preparation_times() -> None:
    ChessPlayer.objects.update(
        meal_type=Case(
            When(type=['Breakfast'], then=Value('10 minutes')),
            When(type=['Lunch'], then=Value('12 minutes')),
            When(type=['Dinner'], then=Value('15 minutes')),
            When(type=['Snack'], then=Value('5 minutes')),
            default=F('meal_type'),
        )
    )


def update_low_calorie_meals() -> None:
    ChessPlayer.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(meals=400)


def update_high_calorie_meals() -> None:
    ChessPlayer.objects.filter(meal_type__in=['Lunch', 'Snack']).update(meals=700)


def delete_lunch_and_snack_meals() -> None:
    ChessPlayer.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons() -> str:
    hard_dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')

    return '\n'.join(str(x) for x in hard_dungeons)


def bulk_create_dungeons(*args) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty=['Easy'], then=Value('The Erased Thomb')),
            When(difficulty=['Medium'], then=Value('The Coral Labyrint')),
            When(difficulty=['Hard'], then=Value('The Lost Haun')),
            default=F('name'),
        )
    )


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exlude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty=['Easy'], then=Value(25)),
            When(difficulty=['Medium'], then=Value(50)),
            When(difficulty=['Hard'], then=Value(75)),
            default=F('recommended_level'),
        )
    )


def update_dungeon_rewards() -> None:
    Dungeon.objects.update(
        reward=Case(
            When(boss_health=500, then=Value('1000 Gold')),
            When(location__startswith='E', then=Value('New dungeon unlocked')),
            When(location__endswith='s', then=Value('Dragonheart Amuled')),
            default=F('reward'),
        )
    )


def set_new_locations() -> None:
    Dungeon.objects.update(
        location=Case(
            When(recommended_level=25, then=Value('Enchanted Maz')),
            When(recommended_level=50, then=Value('Grimstone Mine')),
            When(recommended_level=75, then=Value('Shadowed Abys')),
            default=F('location'),
        )
    )


def show_workouts() -> str:
    calisthenics_crossfit_workouts = Workout.objects.filter(
        workout_type__in=['Calisthenics', 'CrossFit'])

    return '\n'.join(str(n) for n in calisthenics_crossfit_workouts)


def get_high_difficulty_cardio_workouts() -> QuerySet:
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')


def set_new_instructors() -> None:
    Workout.objects.update(
        instructor=Case(
            When(workout_type='Cardio', then=Value('John Smit')),
            When(workout_type='Strength', then=Value('Michael William')),
            When(workout_type='Yoga', then=Value('Emily Johnso')),
            When(workout_type='CrossFit', then=Value('Sarah Davi')),
            When(workout_type='Calisthenics', then=Value('Chris Heria')),
            default=F('instructor'),
        )
    )


def set_new_duration_times() -> None:
    Workout.objects.update(
        duration=Case(
            When(instructor='John Smith', then=Value('15 minutes')),
            When(instructor='Sarah Davis', then=Value('30 minutes')),
            When(instructor='Chris Heria', then=Value('45 minute')),
            When(instructor='Michael William', then=Value('1 hour')),
            When(instructor='Emily Johnson', then=Value('1 hour and 30 minutes')),
            default=F('duration'),
        )
    )


def delete_workouts() -> None:
    Workout.objects.exclude(workout_type__in=['Strength', 'Calisthenics']).delete()
