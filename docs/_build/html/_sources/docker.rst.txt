Docker configuration for easy deployment
----------------------------------------

.. -docker-

To include Docker configuration to your project, adds the ``--docker`` option
to the general djpro project creation command:

.. code-block:: shell

   djpro project YOUR-PROJECT-NAME --docker

.. note::

   Change ``YOUR-PROJECT-NAME`` to your project name.

``djpro`` will create a Django project including API configuration with the following structure:

.. code-block:: shell

    root/
    ├── .env.dev
    ├── .env.prod
    ├── .env.prod.db
    ├── docker-compose.yml
    ├── Dockerfile
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

.. note::

   djpro automatically sets a ``production environment`` when the ``--docker`` option is run,
   you can change this by modifying the ``DJANGO_ENV`` from ``prod`` to ``dev`` in ``config/.env.conf``.

IMPORTANT
---------

Before running your Django project using Docker Compose, you have to set your database
configuration in ``.env.prod`` and ``.env.prod.db``.

.. note::

   ``.env.prod`` contains the environment variables needed to run Django.
   ``.env.prod.db`` contains the environment variables to run the Docker ``db`` container.

Then you can run the project using the following command:

.. code-block:: shell

   docker-compose up --build -d

Aplying migrations and collecting static files:

.. code-block:: shell

   docker-compose exec web python src/bin/manage.py migrate --noinput
   docker-compose exec web python src/bin/manage.py collectstatic

.. note::

   If you want to run the project on local using Docker, then you will have to change to 'True' the DEBUG mode on ``settings_prod.py``.

* `Learn more about Docker <https://docs.docker.com/>`_

.. -end-docker-