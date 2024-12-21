===========
Quick Start
===========

Usage
=====

Start by creating the architecture of a Django project.

Execute the following line of code inside the root folder of your project:

.. code-block:: shell

   djpro project YOUR-PROJECT-NAME

.. note::

   Change ``YOUR-PROJECT-NAME`` to your project name.

``djpro`` will create a Django project with the following structure:

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

Run your Django project executing the following commands inside the folder ``src``:

.. code-block:: shell

   pip install -r requirements.txt
   djpro man collectstatic
   djpro man runserver

Create a new Module
-------------------

.. note::

   We call ``modules`` to the applications contained in your Django project.

You can create a new Module in your existing project executing the following command:

.. code-block:: shell

   djpro module YOUR-MODULE-NAME

.. note::

   Change ``YOUR-MODULE-NAME`` to your Module name.

.. note::

   IMPORTANT: The ``module`` subcommand needs to find the ``src`` folder. Run the command in the root folder of your project.

You can also add the files you want to be created in your module:

.. code-block:: shell

   djpro module YOUR-MODULE-NAME -models -views -urls

.. note::

   This command will create the module folder including the ``models.py``, ``views.py`` and ``urls.py`` files.

.. code-block:: shell

    root/
    └── src/
        └── modules/
            ├── __init__.py
            └── YOUR-MODULE/
                ├── __init__.py
                ├── models/
                │   ├── __init__.py
                │   └── models.py
                ├── urls.py
                └── views/
                    ├── __init__.py
                    └── views.py

See the list of available files:

.. code-block:: shell
   
   -models
   -views
   -serializers
   -urls
   -forms
   -admin
   -apps

Run the develop environment locally
-----------------------------------

.. code-block:: shell

   djpro man runserver

.. note::

   The ``man`` command was created to make it faster and easier to run the ``manage.py`` commands in Django.
   `Find out more about its use <man.html>`.

----

Including API configuration
===========================

.. include:: ./api.rst
   :start-after: -api-
   :end-before: -end-api-

Adding a custom theme for Django Admin Site
===========================================

.. include:: ./unfold.rst
   :start-after: -unfold-
   :end-before: -end-unfold-

Including Docker configuration
==============================

.. include:: ./docker.rst
   :start-after: -docker-
   :end-before: -end-docker-
