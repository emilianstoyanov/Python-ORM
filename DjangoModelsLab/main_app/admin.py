from django.contrib import admin
from .models import MyBook


# Register your models here.


@admin.register(MyBook)
class MyBook(admin.ModelAdmin):
    pass
