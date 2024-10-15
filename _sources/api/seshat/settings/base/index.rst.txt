seshat.settings.base
====================

.. py:module:: seshat.settings.base

.. autoapi-nested-parse::

   The base settings for the Seshat project.

   They are used by the development and production environment settings,
   available in :doc:`/api/seshat/settings/local/index` and
   :doc:`/api/seshat/settings/production/index`.



Attributes
----------

.. autoapisummary::

   seshat.settings.base.ACCOUNT_AUTHENTICATION_METHOD
   seshat.settings.base.ACCOUNT_EMAIL_REQUIRED
   seshat.settings.base.ACCOUNT_LOGOUT_REDIRECT
   seshat.settings.base.ACCOUNT_USERNAME_REQUIRED
   seshat.settings.base.ALLOWED_HOSTS
   seshat.settings.base.AUTHENTICATION_BACKENDS
   seshat.settings.base.AUTH_PASSWORD_VALIDATORS
   seshat.settings.base.BASE_DIR
   seshat.settings.base.CESIUM_ION_ACCESS_TOKEN
   seshat.settings.base.CORS_ALLOWED_ORIGINS
   seshat.settings.base.CSRF_TRUSTED_ORIGINS
   seshat.settings.base.DATABASES
   seshat.settings.base.DEBUG
   seshat.settings.base.DEFAULT_AUTO_FIELD
   seshat.settings.base.EMAIL_BACKEND
   seshat.settings.base.EMAIL_FROM_USER
   seshat.settings.base.GDAL_LIBRARY_PATH
   seshat.settings.base.GEOGRAPHIC_DB
   seshat.settings.base.INSTALLED_APPS
   seshat.settings.base.INTERNAL_IPS
   seshat.settings.base.LANGUAGE_CODE
   seshat.settings.base.LOCALE_PATHS
   seshat.settings.base.LOGIN_REDIRECT_URL
   seshat.settings.base.MEDIA_ROOT
   seshat.settings.base.MEDIA_URL
   seshat.settings.base.MESSAGE_TAGS
   seshat.settings.base.MIDDLEWARE
   seshat.settings.base.MY_CURRENT_SERVER
   seshat.settings.base.RECAPTCHA_PUBLIC_KEY
   seshat.settings.base.REST_FRAMEWORK
   seshat.settings.base.ROOT_URLCONF
   seshat.settings.base.SECRET_KEY
   seshat.settings.base.SECURE_CROSS_ORIGIN_OPENER_POLICY
   seshat.settings.base.SESHAT_ENVIRONMENT
   seshat.settings.base.SITE_ID
   seshat.settings.base.SOCIALACCOUNT_PROVIDERS
   seshat.settings.base.STATICFILES_DIRS
   seshat.settings.base.STATICFILES_STORAGE
   seshat.settings.base.STATICFILES_STORAGE
   seshat.settings.base.STATIC_ROOT
   seshat.settings.base.STATIC_URL
   seshat.settings.base.TEMPLATES
   seshat.settings.base.TIME_ZONE
   seshat.settings.base.USE_I18N
   seshat.settings.base.USE_L10N
   seshat.settings.base.USE_TZ
   seshat.settings.base.WSGI_APPLICATION
   seshat.settings.base.local_env_path


Module Contents
---------------

.. py:data:: ACCOUNT_AUTHENTICATION_METHOD
   :value: 'email'


.. py:data:: ACCOUNT_EMAIL_REQUIRED
   :value: True


.. py:data:: ACCOUNT_LOGOUT_REDIRECT
   :value: 'seshat-index'


.. py:data:: ACCOUNT_USERNAME_REQUIRED
   :value: False


.. py:data:: ALLOWED_HOSTS
   :value: ['seshatdb.herokuapp.com', '127.0.0.1', 'majidbenam.com', 'www.majidbenam.com', 'https://majidbenam.com']


.. py:data:: AUTHENTICATION_BACKENDS
   :value: ['django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend']


.. py:data:: AUTH_PASSWORD_VALIDATORS

   AUTH_PASSWORD_VALIDATORS defines the validators that are used to check the strength of passwords.

.. py:data:: BASE_DIR

.. py:data:: CESIUM_ION_ACCESS_TOKEN

.. py:data:: CORS_ALLOWED_ORIGINS
   :value: ['http://localhost:3000', 'http://127.0.0.1:3000']


   CORS_ALLOWED_ORIGINS defines the allowed origins for Cross-Origin Resource Sharing (CORS).

.. py:data:: CSRF_TRUSTED_ORIGINS
   :value: ['https://majidbenam.com', 'http://*.majidbenam.com', 'http://majidbenam.com',...


   CSRF_TRUSTED_ORIGINS defines the trusted origins for Cross-Site Request Forgery (CSRF) protection.

.. py:data:: DATABASES

   Database settings for local development.

.. py:data:: DEBUG

.. py:data:: DEFAULT_AUTO_FIELD
   :value: 'django.db.models.BigAutoField'


   DEFAULT_AUTO_FIELD is set to `django.db.models.BigAutoField`.

.. py:data:: EMAIL_BACKEND
   :value: 'django.core.mail.backends.smtp.EmailBackend'


.. py:data:: EMAIL_FROM_USER

   The email address from which the emails will be sent.

.. py:data:: GDAL_LIBRARY_PATH
   :value: '/opt/homebrew/opt/gdal/lib/libgdal.dylib'


.. py:data:: GEOGRAPHIC_DB
   :value: True


   GEOGRAPHIC_DB is set to True to enable the geographic database.

.. py:data:: INSTALLED_APPS
   :value: ['seshat.apps.accounts', 'django.contrib.admin', 'django.contrib.auth',...


.. py:data:: INTERNAL_IPS
   :value: ['127.0.0.1']


   INTERNAL_IPS defines the list of IP addresses that are allowed to visit the debug toolbar.

.. py:data:: LANGUAGE_CODE

   LANGUAGE_CODE is set to en-us by default.

.. py:data:: LOCALE_PATHS

   LOCALE_PATHS defines the directories in which Django will search for translation files.

.. py:data:: LOGIN_REDIRECT_URL
   :value: 'seshat-index'


.. py:data:: MEDIA_ROOT

   The absolute path to the directory where uploaded files will be saved.

.. py:data:: MEDIA_URL
   :value: '/media/'


   The URL to use when referring to media files located in the `media` directory.

.. py:data:: MESSAGE_TAGS

.. py:data:: MIDDLEWARE
   :value: ['django.middleware.security.SecurityMiddleware',...


   MIDDLEWARE defines the list of middleware classes that Django will use.

.. py:data:: MY_CURRENT_SERVER
   :value: 'http://127.0.0.1:8000'


.. py:data:: RECAPTCHA_PUBLIC_KEY

.. py:data:: REST_FRAMEWORK

   REST_FRAMEWORK defines the default settings for the Django REST framework.

   The default pagination class is set to `PageNumberPagination` with a page size
   of 1000.

.. py:data:: ROOT_URLCONF
   :value: 'seshat.urls'


   ROOT_URLCONF is set to the URL configuration for the Seshat project.

.. py:data:: SECRET_KEY

.. py:data:: SECURE_CROSS_ORIGIN_OPENER_POLICY
   :value: None


   SECURE_CROSS_ORIGIN_OPENER_POLICY is set to None to disable the Cross-Origin Opener Policy.

.. py:data:: SESHAT_ENVIRONMENT

   The environment in which the Seshat application is running.

   .. note::

      The value is set to `local` by default. This value can be changed in the
      environment variable SESHAT_ENVIRONMENT.

.. py:data:: SITE_ID
   :value: 2


.. py:data:: SOCIALACCOUNT_PROVIDERS

   SOCIALACCOUNT_PROVIDERS defines the social account providers for the Django all-auth package.

.. py:data:: STATICFILES_DIRS

   Defines the directories in which Django will search for additional static files.

.. py:data:: STATICFILES_STORAGE
   :value: 'whitenoise.storage.CompressedManifestStaticFilesStorage'


   The static files storage is set to the whitenoise storage, which is a compressed manifest static files storage.

.. py:data:: STATICFILES_STORAGE
   :value: 'django.contrib.staticfiles.storage.StaticFilesStorage'


   The static files storage is set to the Django static files storage for testing environments.

   :noindex:

.. py:data:: STATIC_ROOT

   The absolute path to the directory where `collectstatic` will collect static files for deployment.

   .. note:: The value set here is the `static` directory in the base directory of the project.

.. py:data:: STATIC_URL
   :value: 'static/'


   The URL to use when referring to static files located in the `static` directory.

.. py:data:: TEMPLATES

   TEMPLATES defines the list of engines that Django can use to render templates.

.. py:data:: TIME_ZONE

   TIME_ZONE is set to UTC by default.

.. py:data:: USE_I18N
   :value: True


   USE_I18N is set to True to enable internationalization.

.. py:data:: USE_L10N
   :value: True


   USE_L10N is set to True to enable localization.

.. py:data:: USE_TZ
   :value: True


   USE_TZ is set to True to enable time zone support.

.. py:data:: WSGI_APPLICATION
   :value: 'seshat.wsgi.application'


   WSGI_APPLICATION is set to the WSGI application for the Seshat project.

.. py:data:: local_env_path

