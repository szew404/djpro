===========
Man command
===========

Usage
=====

This command was created to make it faster and easier to run the ``manage.py`` commands in Django.

.. note::

   This command must be used from the root folder of your project. The command will search for the ``/src/bin`` directory.

This command allows you to execute any command available in manage.py.
View list of available manage.py commands:

.. code-block:: shell

   djpro man help

Examples
========

.. code-block:: shell

   djpro man runserver

.. code-block:: shell

   djpro man migrate

.. note::

   Behind the scenes, the ``man`` command executes in the terminal ``python manage.py <command>``.