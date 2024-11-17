============
Installation
============

Requirements
============

* `Django <https://www.djangoproject.com/>`_ >= 5.1

Installing djpro
=================

djpro is a Python-only package `hosted_on_pypi`_.
The recommended installation method is `pip`_-installing into a
:mod:`virtualenv <python:venv>`:

.. code-block:: console

   $ python -m pip install djpro

.. note::

   djpro will install ``Django 5.1 version`` if is not installed yet.


.. _hosted_on_pypi: #
.. _pip: https://pip.pypa.io/en/stable/


Unstable version
================

The master of all the material is the Git repository at https://github.com/szew404/dj-pro.
So, you can also install the latest unreleased development version directly from the
``develop`` branch on GitHub. It is a work-in-progress of a future stable release so the
experience might be not as smooth:

.. code-block:: console

   $ pip install --upgrade https://github.com/szew404/dj-pro

This command will download the latest version of dj-pro and install
it to your system.

.. note::

   The ``develop`` branch will always contain the latest unstable version, so the experience
   might be not as smooth.

More information about ``pip`` and PyPI can be found here:

* `Install pip <https://pip.pypa.io/en/latest/installing/>`_
* `Python Packaging User Guide <https://packaging.python.org/en/latest/>`_