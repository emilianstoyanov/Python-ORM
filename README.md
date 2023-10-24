# Python-ORM

```
ORM - Object Relational Mapping
```

[Django Documentation](https://docs.djangoproject.com/en/4.2/)


## Django Commands:


### 1. Creating a New Django Project:
``
    django-admin startproject <projectname>
``


### 2. Creating a New Django App:

``
    python manage.py startapp <appname>
``
### 3. Running the Development Server:

``
    python manage.py runserver
``

### 4. Creating Database Tables:

``
    python manage.py makemigrations
``

``
    python manage.py migrate
``
### 5. Creating a Superuser (Admin User):

``
    python manage.py createsuperuser
``
### 6. Collecting Static Files:

``
    python manage.py collectstatic
``

### 7. Creating a New Migration:

``
   python manage.py makemigrations <appname>
``

### 8. Applying Migrations:

``
   python manage.py migrate <appname>
``


### 9. Creating a New Django User:

``
   python manage.py migrate <appname>
``

### 10. Starting a Django Shell:

``
  python manage.py shell
``

### 11. Creating a Custom Management Command:

``
  python manage.py create_command my_custom_command
``
### 12. Running Tests:

``
 python manage.py test appname
``

### 13. Creating empty migration file:

``
python .\manage.py makemigrations <main_app> --name  <migrate_age_group> --empty
``

 
## Example:


        from django.db import migrations


        def set_age_group(apps, schema_editor):
            person_model = apps.get_model('main_app', 'Person')

            persons = person_model.objects.all()

            for person_record in persons:
                if person_record.age <= 12:
                    person_record.age_group = 'Child'
                elif person_record.age <= 17:
                    person_record.age_group = 'Teen'
                else:
                    person_record.age_group = 'Adult'

            # We save changes to the base once, not every iteration
            person_model.objects.bulk_update(persons, ['age_group'])


        def set_age_group_default(apps, schema_editor):
            person_model = apps.get_model('main_app', 'Person')

            age_group_default = person_model._meta.get_field('age_group').default

            for person in person_model.objects.all():
                person.age_group = age_group_default
                person.save()


        # python .\manage.py makemigrations main_app --name  migrate_age_group --empty
        class Migration(migrations.Migration):
            dependencies = [
                ('main_app', '0009_person'),
            ]

            operations = [
                migrations.RunPython(set_age_group, reverse_code=set_age_group_default)
            ]

    1. Create an empty migration file.
        python .\manage.py makemigrations main_app --name  migrate_age_group --empty
    2. We create a function  for the specific purpose of changing the database.
    3. We execute the command: python manage.py migrate
    4. If we want to revert the changes, we run the command: python manage.py migrate main_app <name of previous migration>

    
    

## Django ORM Commands:

### 1. Creating a New Model: 
     Define your model in the app's models.py file, then create a migration and apply it.

### 2. Querying the Database: 
     You can use Django's QuerySet API to retrieve data from the database. For example:

``
    from appname.models import ModelName  
``

``
    data = ModelName.objects.all()
``

### 3. Filtering Data:

``
 data = ModelName.objects.filter(fieldname=value)
``

### 4. Creating New Records:

``
 new_record = ModelName(field1=value1, field2=value2)
``

``
 new_record.save()
``

### 5. Updating Records:

``
    record = ModelName.objects.get(pk=pk)
``

``
    record.field1 = new_value
``

``
    record.save()
``

### 6. Deleting Records:

``
    record = ModelName.objects.get(pk=pk)
``

``
    record.delete()
``