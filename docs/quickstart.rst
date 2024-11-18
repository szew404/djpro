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
        │       ├── models.py
        │       ├── serializers.py
        │       ├── urls.py
        │       └── views.py
        ├── static/
        ├── tests/
        ├── templates/
        └── utils/
            └── __init__.py

Run your Django project executing the following commands inside the folder ``src``:

.. code-block:: shell

   pip install -r requirements.txt
   python bin/manage.py collectstatic
   python bin/manage.py runserver

Create a new Module
-------------------

.. note::

   We call ``modules`` to the applications contained in your Django project.

You can create a new Module executing the following commands:

.. code-block:: shell

   cd src/modules
   mkdir YOUR-MODULE-NAME

.. note::

   Change ``YOUR-MODULE-NAME`` to your Module name.

Create a new ``__init__.py`` file inside your Module folder and add your new Module to ``INSTALED_APPS`` in ``config/settings_base``.

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
