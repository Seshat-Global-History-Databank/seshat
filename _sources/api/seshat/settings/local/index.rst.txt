seshat.settings.local
=====================

.. py:module:: seshat.settings.local

.. autoapi-nested-parse::

   Settings for local development of the Seshat project.
   Also used for non-production cloud development environments.
   Also used for GitHub Actions testing.



Attributes
----------

.. autoapisummary::

   seshat.settings.local.ALLOWED_HOSTS
   seshat.settings.local.CESIUM_ION_ACCESS_TOKEN
   seshat.settings.local.DATABASES
   seshat.settings.local.GDAL_LIBRARY_PATH
   seshat.settings.local.MIDDLEWARE
   seshat.settings.local.STATICFILES_STORAGE
   seshat.settings.local.django_settings_module
   seshat.settings.local.my_current_server


Module Contents
---------------

.. py:data:: ALLOWED_HOSTS
   :value: ['127.0.0.1', '51.141.239.61', 'localhost']


   Set ALLOWED_HOSTS to allow the server to run without a domain name for local testing.

.. py:data:: CESIUM_ION_ACCESS_TOKEN

.. py:data:: DATABASES

   Database settings for GitHub Actions.

   :noindex:

.. py:data:: GDAL_LIBRARY_PATH
   :value: '/usr/lib/libgdal.so'


.. py:data:: MIDDLEWARE
   :value: ['django.middleware.security.SecurityMiddleware',...


   MIDDLEWARE defines the list of middleware classes that Django will use.

.. py:data:: STATICFILES_STORAGE
   :value: 'django.contrib.staticfiles.storage.StaticFilesStorage'


   Specifies static files storage for testing environments.

   :noindex:

.. py:data:: django_settings_module

.. py:data:: my_current_server
   :value: '127.0.0.1:8000'


