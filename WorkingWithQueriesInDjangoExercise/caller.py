import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtWorkGallery


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


