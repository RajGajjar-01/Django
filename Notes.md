## How to use run script command --> Provided by django_extensions

1. create a script folder in your app
2. create a file for example create_script.py
3. override run method in that script 

* Example -> def run():
                pass
        
3. command: <code>python manage.py runscript create_script</code>

# March 8th 2025

## save method in django models and _state object

The _state attribute refers to a ModelState object that tracks the lifecycle of the model instance.

The ModelState object has two attributes: adding, a flag which is True if the model has not been saved to the database yet, and db, a string referring to the database alias the instance was loaded from or saved to.

Newly instantiated instances have adding=True and db=None, since they are yet to be saved. Instances fetched from a QuerySet will have adding=False and db set to the alias of the associated database.

## update() method in django models

It updates existing model instance or whole queryset.
It does not call any save() method and it does not emit any signals eg. post_save

## delete() method in django models

It deletes particular modal instance in database
It returns a tuple containing count of how many records that has been deleted and dictionary of how much records got deleted from which table.