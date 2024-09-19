"""
The base settings for the Seshat project.

They are used by the development and production environment settings,
available in :doc:`/api/seshat/settings/local/index` and
:doc:`/api/seshat/settings/production/index`.
"""

__all__ = [
    "MESSAGE_TAGS",
    "BASE_DIR",
    "SECRET_KEY",
    "DEBUG",
    "MY_CURRENT_SERVER",
    "ALLOWED_HOSTS",
    "INSTALLED_APPS",
    "AUTHENTICATION_BACKENDS",
    "RECAPTCHA_PUBLIC_KEY",
    "RECAPTCHA_PRIVATE_KEY",
    "LOGIN_REDIRECT_URL",
    "ACCOUNT_LOGOUT_REDIRECT",
    "SITE_ID",
    "EMAIL_BACKEND",
    "ACCOUNT_EMAIL_REQUIRED",
    "ACCOUNT_USERNAME_REQUIRED",
    "ACCOUNT_AUTHENTICATION_METHOD",
    "SOCIALACCOUNT_PROVIDERS",
    "DEFAULT_AUTO_FIELD",
    "ROOT_URLCONF",
    "INTERNAL_IPS",
    "WSGI_APPLICATION",
    "MIDDLEWARE",
    "TEMPLATES",
    "DATABASES",
    "AUTH_PASSWORD_VALIDATORS",
    "CSRF_TRUSTED_ORIGINS",
    "LANGUAGE_CODE",
    "TIME_ZONE",
    "USE_I18N",
    "USE_L10N",
    "USE_TZ",
    "LOCALE_PATHS",
    "EMAIL_FROM_USER",
    "EMAIL_HOST",
    "EMAIL_HOST_USER",
    "EMAIL_HOST_PASSWORD",
    "EMAIL_USE_TLS",
    "EMAIL_PORT",
    "STATIC_URL",
    "STATIC_ROOT",
    "STATICFILES_DIRS",
    "STATICFILES_STORAGE",
    "MEDIA_URL",
    "MEDIA_ROOT",
    "SESHAT_ENVIRONMENT",
    "REST_FRAMEWORK",
    "CORS_ALLOWED_ORIGINS",
    "GEOGRAPHIC_DB",
    "GDAL_LIBRARY_PATH",
    "GEOS_LIBRARY_PATH",
    "SECURE_CROSS_ORIGIN_OPENER_POLICY",
]

import os
import django_heroku
import sys

from django.contrib.messages import constants as messages
from pathlib import Path
from decouple import config


MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

_local_env_path = str(Path.cwd()) + "/seshat/settings/.env"
_local_env_path_exists = os.path.exists(_local_env_path)
_is_github_action = os.getenv("GITHUB_ACTIONS") == "true"

# BASE_DIR is calculated based on this file (base.py) and then goes to parents above.
BASE_DIR = Path(__file__).resolve().parent.parent

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Django's secret key is used to provide cryptographic signing for cookies and other
# security mechanisms
SECRET_KEY = config(
    "SECRET_KEY", default="django-insecure$seshat.settings.local"
)

# DEBUG is a boolean that turns on/off debug mode for Django
DEBUG = config("DEBUG", default=True, cast=bool)

# MY_CURRENT_SERVER is the current server that the application is running on
MY_CURRENT_SERVER = "https://www.majidbenam.com"

if DEBUG:
    MY_CURRENT_SERVER = "http://127.0.0.1:8000"

# ALLOWED_HOSTS is a list of strings representing the host/domain names that this Django
# site can serve
ALLOWED_HOSTS = [
    "seshatdb.herokuapp.com",
    "127.0.0.1",
    "majidbenam.com",
    "www.majidbenam.com",
    "https://majidbenam.com",
]

# Define the installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Add this
    "django.contrib.humanize",
    "crispy_forms",
    "whitenoise.runserver_nostatic",
    "seshat.apps.accounts",
    "seshat.apps.core",
    "seshat.apps.general",
    "seshat.apps.sc",
    "seshat.apps.wf",
    "seshat.apps.rt",
    "seshat.apps.crisisdb",
    "seshat.apps.seshat_api",
    "django_filters",
    "corsheaders",
    "rest_framework",
    "mathfilters",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django.contrib.gis",
    "leaflet",
    "django_extensions",
]

# Define the authentication backends:
# - django.contrib.auth.backends.ModelBackend is needed to login by username in Django admin
# - allauth.account.auth_backends.AuthenticationBackend is needed for all-auth specific
#   authentication methods
# - allauth.socialaccount.auth_backends.AuthenticationBackend can potentially be added for
#   all-auth social account authentication methods -- see the all-auth documentation for
#   more
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

# all-auth settings
LOGIN_REDIRECT_URL = "seshat-index"
ACCOUNT_LOGOUT_REDIRECT = "seshat-index"
SITE_ID = 2
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# Social account providers (all-auth)
SOCIALACCOUNT_PROVIDERS = {}
if (
    not _local_env_path_exists
    and not _is_github_action
):
    SOCIALACCOUNT_PROVIDERS = {
        "google": {
            "APP": {
                "client_id": config("GOOGLE_APP_CLIENT_ID"),
                "secret": config("GOOGLE_APP_SECRET_KEY"),
                "redirect_uris": [
                    "http://seshatdata.com/accounts/google/login/callback/",
                    "http://localhost",
                ],
                # 'key': ''
            },
            "SCOPE": [
                "profile",
                "email",
            ],
            "AUTH_PARAMS": {
                "access_type": "online",
            },
        }
    }
    """SOCIALACCOUNT_PROVIDERS defines the social account providers for the Django all-auth package."""  # noqa: E501 pylint: disable=C0301

# Google reCAPTCHA settings
RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY = "", ""
if (
    not _local_env_path_exists
    and not _is_github_action
):
    RECAPTCHA_PUBLIC_KEY = config("GOOGLE_RECAPTCHA_SITE_KEY")
    RECAPTCHA_PRIVATE_KEY = config("GOOGLE_RECAPTCHA_SECRET_KEY")
    INSTALLED_APPS.append("django_recaptcha")

# Default auto field specifies the type of primary key that will be used for all models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
"""DEFAULT_AUTO_FIELD is set to `django.db.models.BigAutoField`."""

# Root URL configuration defines the starting point for URL configurations
ROOT_URLCONF = "seshat.urls"
"""ROOT_URLCONF is set to the URL configuration for the Seshat project."""

# Internal IPs defines the list of IP addresses that are allowed to visit the debug toolbar
INTERNAL_IPS = ["127.0.0.1"]
"""INTERNAL_IPS defines the list of IP addresses that are allowed to visit the debug toolbar."""  # noqa: E501 pylint: disable=C0301

# WSGI application defines the WSGI application for the Seshat project
WSGI_APPLICATION = "seshat.wsgi.application"
"""WSGI_APPLICATION is set to the WSGI application for the Seshat project."""

# Django's middleware classes are used to modify the request/response objects
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
"""MIDDLEWARE defines the list of middleware classes that Django will use."""

# Django's template engine settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "seshat.apps.core.context_processors.notifications",
            ],
        },
    },
]
"""TEMPLATES defines the list of engines that Django can use to render templates."""

# Settings for the database
DATABASES = {}
if (
    not _local_env_path_exists
    and not _is_github_action
):
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": "localhost",
            "PORT": 5432,
        }
    }
    """
    Database settings for local development.
    """

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
"""
AUTH_PASSWORD_VALIDATORS defines the validators that are used to check the strength of passwords.
"""  # noqa: E501 pylint: disable=C0301

# Define the trusted origins for CSRF protection. The most important one is the last one.
CSRF_TRUSTED_ORIGINS = [
    "https://majidbenam.com",
    "http://*.majidbenam.com",
    "http://majidbenam.com",
    "https://seshatdb.herokuapp.com",
    "http://seshatdb.herokuapp.com",
    "https://*.majidbenam.com",
]
"""CSRF_TRUSTED_ORIGINS defines the trusted origins for Cross-Site Request Forgery (CSRF) protection."""  # noqa: E501 pylint: disable=C0301

# Internationalization
LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")
"""LANGUAGE_CODE is set to en-us by default."""

TIME_ZONE = config("TIME_ZONE", default="UTC")
"""TIME_ZONE is set to UTC by default."""

USE_I18N = True
"""USE_I18N is set to True to enable internationalization."""

USE_L10N = True
"""USE_L10N is set to True to enable localization."""

USE_TZ = True
"""USE_TZ is set to True to enable time zone support."""

LOCALE_PATHS = [BASE_DIR / "locale"]
"""LOCALE_PATHS defines the directories in which Django will search for translation files."""  # noqa: E501 pylint: disable=C0301

# Email config BACKUP:
(
    EMAIL_FROM_USER,
    EMAIL_HOST,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD,
    EMAIL_USE_TLS,
    EMAIL_PORT,
) = (  # noqa: E501 pylint: disable=C0301
    "",
    "",
    "",
    "",
    "",
    587,
)

if (
    not _local_env_path_exists
    and not _is_github_action
):
    EMAIL_FROM_USER = config("EMAIL_FROM_USER")
    """The email address from which the emails will be sent."""
    EMAIL_HOST = config("EMAIL_HOST")
    """The email host."""
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    """The email host user."""
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    """The email host password."""
    EMAIL_USE_TLS = True
    """Defines whether email will use TLS."""
    EMAIL_PORT = 587
    """The email port."""

STATIC_URL = "static/"
"""
The URL to use when referring to static files located in the `static` directory.
"""

STATIC_ROOT = BASE_DIR.parent.parent / "static"
"""
The absolute path to the directory where `collectstatic` will collect static files for
deployment.

Note:
    The value set here is the `static` directory in the base directory of the project.
"""

STATICFILES_DIRS = [BASE_DIR / "static"]
"""
Defines the directories in which Django will search for additional static files.
"""

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
"""
The static files storage is set to the whitenoise storage, which is a compressed
manifest static files storage.
"""

if "test" in sys.argv:
    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )
    """
    The static files storage is set to the Django static files storage for testing
    environments.

    :noindex:
    """

MEDIA_URL = "/media/"
"""The URL to use when referring to media files located in the `media` directory."""

MEDIA_ROOT = BASE_DIR.parent.parent / "media"
"""The absolute path to the directory where uploaded files will be saved."""

SESHAT_ENVIRONMENT = config("SESHAT_ENVIRONMENT", default="local")
"""
The environment in which the Seshat application is running.

Note:
    The value is set to `local` by default. This value can be changed in the
    environment variable SESHAT_ENVIRONMENT.
"""

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 1000,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}
"""
REST_FRAMEWORK defines the default settings for the Django REST framework.

The default pagination class is set to `PageNumberPagination` with a page size
of 1000.
"""

# CORS ALLOWED ORIGINS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
"""CORS_ALLOWED_ORIGINS defines the allowed origins for Cross-Origin Resource Sharing (CORS)."""  # noqa: E501 pylint: disable=C0301

django_heroku.settings(locals())

GEOGRAPHIC_DB = True
"""GEOGRAPHIC_DB is set to True to enable the geographic database."""

if sys.platform.startswith("darwin"):
    # macOS settings
    GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
    GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"
else:
    # Linux settings
    if _is_github_action:
        GDAL_LIBRARY_PATH = "/usr/lib/libgdal.so"
        GEOS_LIBRARY_PATH = "/usr/lib/x86_64-linux-gnu/libgeos_c.so"
    else:
        GDAL_LIBRARY_PATH = "/usr/lib/libgdal.so.30"
        # TODO: find a way to specify this based on the VM: aarch64 or x86_64
        # GEOS_LIBRARY_PATH = '/usr/lib/aarch64-linux-gnu/libgeos_c.so'
        GEOS_LIBRARY_PATH = "/usr/lib/x86_64-linux-gnu/libgeos_c.so"

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
"""
SECURE_CROSS_ORIGIN_OPENER_POLICY is set to None to disable the Cross-Origin Opener Policy.
"""
