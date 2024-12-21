===========
Explanation
===========

Why use djpro?
--------------
Django’s Command Line Interface (CLI) is a powerful tool for generating well-structured Django projects.
However, maintaining that clean structure can become challenging as we create multiple
apps, models, templates, views, and routes.


The Default Structure
---------------------

.. code-block:: shell

    project/
    ├── manage.py
    ├── requirements.txt
    ├── project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── app/
        ├── migrations/
        │   └── __init__.py
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── tests.py
        └── views.py

When we create an app in Django, a folder is made with the name of the app,
and typically, it consists of a migrations folder and several files to configure
the admin, models, tests, and views.

While it is an excellent structure already, the problem arises when the project grows.
Imagine a project with 80+ models. So, we can’t have a single Python file with thousands of lines.
It becomes a lot less readable.

Something similar happens with templates.
You’ll need paths like my_app/templates/my_app/template.html, which can feel repetitive.
Switching between app directories can be tedious when managing multiple templates.

When we talk about applications, we find ourselves in the same situation.
As our project grows, understanding the structure becomes more and more complicated.

The solution
------------

In-Project App Location: All our applications live in a central folder called “modules”.
This method allows us to keep our applications organized and separated.

Organizing Models and Views: Over time, the original problem revolved around the increasing size of
our Django project’s models and view files. Django doesn’t strictly enforce placing all models inside
the models.py file. Organizing models and views by placing them in separate files within dedicated
directories. By adopting this approach, we maintain a clean and modular project structure,
ensuring that our models and views remain organized and readable as our project grows.

In-Project Template Location: In this method, all templates live in one central templates
folder at the project level. Each app gets its own subdirectory within this folder.

With the same thinking in mind, we organized each Django directory and went
from a structure that is difficult to scale, to an organized, simple structure
that allows us to scale.

.. code-block:: shell

    root/
    ├── .env.dev
    ├── .gitignore
    ├── requirements.txt
    └── src/
        ├── bin/
        │   ├── __init__.py
        │   └── manage.py
        ├── config/
        │   ├── .env.conf
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings_base.py
        │   ├── settings_dev.py
        │   ├── settings_prod.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── modules/
        │   ├── __init__.py
        │   └── authentication/
        │       ├── __init__.py
        │       ├── models/
        │       │   ├── __init__.py
        │       │   └── auth_model.py
        │       ├── serializers/
        │       │   ├── __init__.py
        │       │   └── login_serializer.py
        │       ├── urls.py
        │       └── views/
        │           ├── __init__.py
        │           └── login.py
        ├── static/
        ├── tests/
        ├── templates/
        └── utils/
            └── __init__.py