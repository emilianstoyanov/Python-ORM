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