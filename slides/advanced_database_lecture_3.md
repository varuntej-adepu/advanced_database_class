
# Advanced Database
## Lecture 3
## Web App, ORM

---

# Agenda

1. Administrative stuff

1. Finish the _ToDo_ app

1. Learn about Object-Relational Mapping

1. Convert the web app to Peewee ORM

---

# Administrative Stuff

1. Blackboard is fixed.

1. Homework to follow.

1. Today's code will be posted on GitHub

    - Details in the homework
  
1. I have to do the _Academic Presence Verification_

    - That means you have to submit an assignment 
    - _Before Wednesday_
    - _Any assignment_

---

# Finish the _Todo_ app

1. **We will use the BottlePy tutorial.**

    - Located here:

         http://bottlepy.org/docs/dev/tutorial_app.html

2. **We will move that tutorial to PythonAnywhere**

    - There are a few code changes

---

# Demo Time

---


# Object-Relational Mapping

Creating a connection between

- using an item as an object

- storing an item as relational table records

---

# Relational Databases

- Tables

- Records

- Fields

- Keys

- Foreign Keys

- Operations

---

# Classes and Objects

- Classes

- Instance

- Properties

- Validity

- Methods

---

# Mapping

```
Classes     --> Tables

Instance    --> Record

Properties  --> Fields

Validity    --> Keys

Methods     --> Operations
```
---

# Peewee ORM 

_Peewee_ is a very popular Python ORM

    - It performs well
    
    - It is very easy to use

    - http://docs.peewee-orm.com/en/latest/

---

# Create a Table

```
from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.
```

---

# Create a Keyed Table

```
class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database
```

---

# Create a Record

```
uncle_bob = Person(name='Bob', 
                   birthday=date(1960, 1, 15), 
                   is_relative=True)

uncle_bob.save() # bob is now stored in the database

```

---

# Update a Record

```
uncle_bob.name = 'Robert'

uncle_bob.save() # bob is now updated in the database
```

---

# Add a Record with a Foreign Key

```
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
```

---

# Delete a Record

```
herb_mittens.delete_instance()
```

---

# Search for a Record

```
uncle_robert = Person.select().where(Person.name == 'Robert').get()
```

---

# Demo Time

