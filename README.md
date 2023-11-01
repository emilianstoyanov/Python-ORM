# Python-ORM

```
ORM - Object Relational Mapping
```

[Django Documentation](https://docs.djangoproject.com/en/4.2/)

[Django Extensions Documentation](https://django-extensions.readthedocs.io/en/latest/)


## How to Start Django Project with a Database(PostgreSQL):

* Navigate to settings.py
* Approximately, in line 76 of code, this is the database config part
* Copy the code below, then change it to your corresponding parameters



```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": '',
        "USER": '',
        "PASSWORD": '',
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

* **NAME** → Database name e.g. django-project previously created in pgAdmin
 <img width="667" alt="image" src="https://github.com/emilianstoyanov/Python-ORM/assets/68276889/b0bcf050-8686-4b26-bcfd-dcd59a0b3f0a">


* **USER** → Database username (default is postgres)
* **PASSWORD** → Database password
* **HOST** → Database host (In development stage, use localhost or IP Address 127.0.0.1 also available)
* **PORT** → The port that used to run the database (Default port is 5432)


## Hide Name, Username, Password and SECRET_KEY
* 1.Create in your project a file named **.env**
<img width="667" alt="image" src="https://github.com/emilianstoyanov/Python-ORM/assets/68276889/00c235b0-3d44-45bb-9b43-3e1f95931b6e">

* 2.Add this to the file:

    ```python
    DATABASES_NAME = 'working-queries-django-lab'
    DATABASES_USER = 'postgres'
    DATABASES_PASSWORD = '1234'
    MY_OWN_KEY = 'django-insecure-cd!p_@ut(kc8)%b_*@)i@kff^oGFrkvy=!c#i!lk9'
    ```
* 3.Change the data with yours in the variables!!!

    - DATABASES_NAME
    - DATABASES_USER
    - DATABASES_PASSWORD
    - MY_OWN_KEY
 
* 4.After adding the .env file, the database settings should look like this:

     ```python
    SECRET_KEY = config('MY_OWN_KEY')
    ```
    
    ```python
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config('DATABASES_NAME'),
            "USER": config('DATABASES_USER'),
            "PASSWORD": config('DATABASES_PASSWORD'),
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    ```
   

* 5.In your settings.py file add:
    - `from decouple import config`
* 6.Run in the Terminal:
    - pip install python-decouple

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
python manage.py makemigrations <main_app> --name  <migrate_age_group> --empty
```
 
### 14. Edit the Data Migration:

`Open the generated data migration file and modify it to use `RunPython` with a custom Python function.`

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
```

## Django ORM Commands:

### 1. Creating a New Model: 
     Define your model in the app's models.py file, then create a migration and apply it.

### 2. Querying the Database: 
#### You can use Django's QuerySet API to retrieve data from the database. For example:

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

#### Оptimized solution:
```python 
def decodes_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(x) - 3) for x in text) # -> Wash the dishes!
    Model.objects.filter(title=task_title).update(description=decoded_text)

encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")
```
#### Non-optimized solution:
```python
tasks_with_matching_title = Model.objects.filter(title=task_title)
decoded_text = ''.join(chr(ord(x) - 3) for x in text)

    for task in tasks_with_matching_title:
        task.description = decoded_text
        task.save()

encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")

```

#### Before:

<img width="405" alt="image" src="https://github.com/emilianstoyanov/Python-ORM/assets/68276889/60582671-4604-4ed9-b0c1-9ee3fa121760">

#### After:

<img width="405" alt="image" src="https://github.com/emilianstoyanov/Python-ORM/assets/68276889/ba3f2eab-ecff-4786-a161-bf8132753c9b">

**Note: `Filters by title "Simple task", changes description to "Zdvk#wkh#glvkhv$", which decodes to "Wash the dishes!'`**

### 10. Update characteres: 

```python
# If the class name is "Mage" - increase the level by 3 and decrease the intelligence by 7.
Model.objects.filter(calss_name="Mage").update(
    level=F('level') + 3,
    intelligence=F('intelligence') - 7,
)

# If the class name is "Warrior" - decrease the hit points by half and increase the dexterity by 4.
Model.objects.filter(class_name="Warrior").update(
    hit_points=F('hit_points') / 2,
    dexterity=F('dexterity') + 4
)

# If the class name is "Assassin" or "Scout" - update their inventory to "The inventory is empty".
Model.objects.filter(class_name__in=["Assassin", "Scout"]).update(
    inventory="The inventory is empty",
)
```
**Note: `An F() object represents the value of a model field, transformed value of a model field, or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory. Instead, Django uses the F() object to generate an SQL expression that describes the required operation at the database level.`**


### 11. Update a field in the database of a specific model. With SQL query and Python ORM on database column named "class_name" with value "Mage": 


```SQL

SQL query:

        UPDATE <model>
        SET level = level + 3
        WHERE class_name = "Mage";  


Python ORM:

        Model.objects.filter(calss_name="Mage").update(
            level=F('level') + 3,
        )
``` 


### 12. Filter by two parameters: 

```python
best_artwork = Model.objects.order_by('-rating', 'id').first()
```
- **'-rating':** Filter by the 'rating' field and take the entry with the highest rating.
- **'id'**: If all records have the same rating then filter and take the record with the highest 'id'.


### 13. Deletes all objects that have a negative rating. 0 (zero) is considered positive:

```python
Model.objects.filter(rating__lt=0).delete()
```
* rating__lt < 0 (delete all entries below zero)
* ratin <= 0 (delete all entries below zero including zero)


### 14. Update the storage of the brand if it is 'Lenovo' or 'Asus':

```python
Model.objects.filter(Q(brand='Lenovo') | Q(brand='Asus')).update(storage=512)
```

```python
Model.objects.filter(brand_in=['Lenovo', 'Asus']).update(storage=512)
```

**Note: `The database field names are 'brand' and 'storage`**


### 15. Updates the operation system for every laptop:

```python
Laptop.objects.filter(brand=['Asus']).update(operation_system='Windows')
Laptop.objects.filter(brand=['Apple']).update(operation_system='MacOS')
Laptop.objects.filter(brand__in=['Dell', 'Acer']).update(operation_system='Linux')
Laptop.objects.filter(brand=['Lenovo']).update(operation_system='Chrome OS')
```

#### Optimization:
```python
Laptop.objects.update(
    operation_system=Case(
        When(brand=['Asus'], then=Value('Windows')),
        When(brand=['Apple'], then=Value('MacOS')),
        When(brand=['Dell', 'Acer'], then=Value('Linux')),
        When(brand=['Lenovo'], then=Value('Chrome OS')),
        default=F('operation_system')
    )
)
```
**Note: `It checks the laptop brand and records the specific operating system.`**