"""
Settings for local development of the Seshat project.
Also used for non-production cloud development environments.
Also used for GitHub Actions testing.
"""

# flake8: noqa

from .base import *
import environ
import os
import sys


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

# Override the default middleware settings in the base.py file to include the GZipMiddleware, AutoLoginMiddleware, and AuthenticationMiddleware.
# This ensures that the environment looks as it would for a logged-in user.
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
    "django.middleware.gzip.GZipMiddleware",
    "seshat.apps.core.middleware.AutoLoginMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",

]
"""MIDDLEWARE defines the list of middleware classes that Django will use."""

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

# We use the local database for development and the GitHub Actions database for testing
if os.getenv('GITHUB_ACTIONS') == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
            'PASSWORD': 'postgres'
        }
    }
    """
    Database settings for GitHub Actions.

    :noindex:
    """
else:

    # Initialise environment variables
    env = environ.Env()
    environ.Env.read_env()

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER') or 'postgres',
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
            'PASSWORD': env('DB_PASSWORD')
        }
    }
    """
    Database settings for local development.

    :noindex:
    """

django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')

my_current_server = "127.0.0.1:8000"

ALLOWED_HOSTS = ['127.0.0.1',
                 '51.141.239.61', # Azure VM @ ATI
                 'localhost']
"""Set ALLOWED_HOSTS to allow the server to run without a domain name for local testing."""

if 'test' in sys.argv:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    """
    Specifies static files storage for testing environments.

    :noindex:
    """

if not sys.platform.startswith('darwin'): # macOS
    # Linux (note: this overrides the path in base.py used by the production environment and may be related to a difference in the way the GDAL library is installed on the ATI and CSH servers, rather than a general difference between local and production environments)
    GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'  

# Cesium
if os.getenv('GITHUB_ACTIONS') != 'true' and 'test' not in sys.argv:
    CESIUM_ION_ACCESS_TOKEN = env('CESIUM_ION_ACCESS')