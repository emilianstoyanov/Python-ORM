# Python-ORM

```
ORM - Object Relational Mapping
```

[Django Documentation](https://docs.djangoproject.com/en/4.2/)

[Django Extensions Documentation](https://django-extensions.readthedocs.io/en/latest/)

## Django Commands:


### 1.  Creating a New Django Project:

```python
django-admin startproject <projectname>
```


### 2. Creating a New Django App:

```python
python manage.py startapp <appname>
```

### 3. Running the Development Server:

```python
python manage.py runserver
```

### 4. Creating Database Tables:

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```
### 5. Creating a Superuser (Admin User):

```python
python manage.py createsuperuser
```

### 6. Collecting Static Files:

```python
python manage.py collectstatic
```

### 7. Creating a New Migration:

```python
python manage.py makemigrations <appname>
```

### 8. Applying Migrations:

```python
python manage.py migrate <appname>
```


### 9. Creating a New Django User:

```python
python manage.py migrate <appname>
```

### 10. Starting a Django Shell:

```python
python manage.py shell
```

### 11. Creating a Custom Management Command:

```python
python manage.py create_command my_custom_command
```
### 12. Running Tests:

```python
python manage.py test appname
```

### 13. Creating empty migration file:

```python
python .\manage.py makemigrations <main_app> --name  <migrate_age_group> --empty
```

 
## Example:

```python 
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


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, reverse_code=set_age_group_default)
    ]

1. Create an empty migration file.
python .\manage.py makemigrations main_app --name  migrate_age_group --empty
2. We create a function for the specific purpose of changing the database.
3. We execute the command: python manage.py migrate
4. If we want to revert the changes, we run the command: python manage.py migrate main_app <name of previous migration>
```

    
    

## Django ORM Commands:

### 1. Creating a New Model: 
     Define your model in the app's models.py file, then create a migration and apply it.

### 2. Querying the Database: 
     You can use Django's QuerySet API to retrieve data from the database. For example:

```python
from appname.models import ModelName  
data = ModelName.objects.all()
```

### 3. Filtering Data:

```python
data = ModelName.objects.filter(fieldname=value)
```

### 4. Creating New Records:

```python
new_record = ModelName(field1=value1, field2=value2)
new_record.save()
```

### 5. Updating Records:

```python
record = ModelName.objects.get(pk=pk)
record.field1 = new_value
record.save()
```

### 6. Deleting Records:

```python
record = ModelName.objects.get(pk=pk)
record.delete()
```

## Useful code:

### 1. Updating the first record in the database: 

```python
Model.objects.filter(pk=1).update(is_capital=True)
```
or
```python
location = Model.objects.first()
location.is_capital = True
location.save()
```

### 2. Retrieves and returns all records from the database in reverse order: 
```python
locations = Model.objects.all().order_by('-id')
return '\n'.join(str(x) for x in locations)
```

### 3. Deletes all entries in the database: 
```python
Model.objects.all().delete()
```

### 4. Deletes the first object: 
```python
Model.objects.first().delete()
```
   
### 5. Deletes the last object: 
```python
Model.objects.last().delete()
```

### 6. Filter by year: 
```python
Model.objects.filter(year__gte=2020).values('price', 'price_with_discount')
```

**Note: `Returns records that have a year after 2020. In the QuerySet, show the price and the price with the discount (fields in the database)`**


### 7. Filter by Boolean value: 
```python
unfinished_task = Model.objects.filter(is_finished=False)
return '\n'.join(str(t) for t in unfinished_task)
```

**Note: `Filters by boolean value. Returns all records for which the is_finished field in the database is False`**

### 8. Filter by odd IDs: 
```python
 for task in Model.objects.all():
    if task.id % 2 != 0:
        task.is_finished = True
        task.save()
```
**Note: `Loops through all objects in the database of the given model.Then it checks if the id is odd. If so, set the field is_finished=True.`**


### 9. Decodes and replaces the text: 

```python
def decodes_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(x) - 3) for x in text) # -> Wash the dishes!
    Task.objects.filter(title=task_title).update(description=decoded_text)


encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")

```

**Note: `Filters by title "Simple task", changes description to "Zdvk#wkh#glvkhv$", which decodes to "Wash the dishes!'`**



