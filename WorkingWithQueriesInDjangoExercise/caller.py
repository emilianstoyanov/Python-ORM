import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtWorkGallery, Laptop, ChessPlayer
from django.db.models import Case, When, Value, F


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


