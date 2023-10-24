from django.contrib import admin
from .models import EventRegistration, Student, Supplier, Person


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'participant_name', 'registration_date']

    list_filter = ['event_name', 'participant_name', 'registration_date']

    search_fields = ['event_name', 'participant_name', 'registration_date']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'grade']

    list_filter = ['date_of_birth', 'age', 'grade']

    search_fields = ['first_name', ]

    # readonly_fields = ['first_name',]

    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'date_of_birth')
        }),

        ('Academic Information', {
            'fields': ('grade',),
            'classes': ('collapse',)

        })
    )

    def __str__(self):
        return self.first_name


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

    list_filter = ['name', 'phone']

    search_fields = ['contact_person', 'email', 'phone']

    list_per_page = 20

    fieldsets = (
        ('Information', {
            'fields': ('name', 'contact_person', 'email', 'address')
        }),
    )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'age_group']

    list_filter = ['name', 'age', 'age_group']

    search_fields = ['name', 'age', 'age_group']
