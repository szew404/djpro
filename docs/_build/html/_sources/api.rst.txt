Django Rest Framework project configuration
-------------------------------------------

.. -api-

To include an API configuration (Django Rest Framework) to your project, adds the ``--api`` option
to the general djpro project creation command:

.. code-block:: shell

   djpro project YOUR-PROJECT-NAME --api

.. note::

   Change ``YOUR-PROJECT-NAME`` to your project name.

``djpro`` will create a Django project including API configuration with the following structure:

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
        │   ├── api/
        │   │   ├── __init__.py
        │   │   ├── models/
        │   │   │   ├── __init__.py
        │   │   │   └── product_model.py 
        │   │   ├── serializers/
        │   │   │   ├── __init__.py
        │   │   │   └── get_product.py
        │   │   ├── urls.py
        │   │   └── views/
        │   │       ├── __init__.py
        │   │       └── get_product.py
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

   djpro includes ``DRF Spectacular`` already configured for your API documentation.
   Find your docs configuration in ``settings_base``.

* `Learn more about Django Rest Framework <https://www.django-rest-framework.org/>`_
* `DRF Spectacular <https://drf-spectacular.readthedocs.io/en/latest/>`_

.. -end-api-