from django.contrib import admin
from .models import EventRegistration, Student


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'participant_name', 'registration_date']
    list_filter = ['event_name', 'participant_name', 'registration_date']
    search_fields = ['event_name', 'participant_name', 'registration_date']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'grade']
    list_filter = ['date_of_birth', 'age', 'grade']
    search_fields = ['first_name']

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'date_of_birth')
        }),

        ('Academic Information', {
            'fields': ('grade',),
            'classes': ('collapse',)

        })
    )
