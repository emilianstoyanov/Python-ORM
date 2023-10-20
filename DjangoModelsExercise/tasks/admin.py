from django.contrib import admin
from .models import Person, Blog, WeatherForecast, Recipe, Product, UserProfile, Book


# Register your models here.
# admin.site.register(Blog)
# admin.site.register(Person)
# admin.site.register(WeatherForecast)
# admin.site.register(Recipe)
# admin.site.register(Product)
# admin.site.register(UserProfile)
# admin.site.register(Book)
# from tasks.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class Recipe(admin.ModelAdmin):
    pass


@admin.register(WeatherForecast)
class WeatherForecast(admin.ModelAdmin):
    pass


@admin.register(Blog)
class Blog(admin.ModelAdmin):
    pass


@admin.register(Person)
class Person(admin.ModelAdmin):
    pass
