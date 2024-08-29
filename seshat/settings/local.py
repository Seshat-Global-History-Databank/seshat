"""
Settings for local development of the Seshat project.
"""

import environ
import os
import sys

from .base import *


# Databases
# We use the local database for development and the GitHub Actions database for testing
if os.getenv("GITHUB_ACTIONS") == "true":
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": "github_actions",
            "USER": "postgres",
            "HOST": "localhost",
            "PORT": "5432",
            "PASSWORD": "postgres",
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
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.postgis",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER") or "postgres",
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
            "PASSWORD": env("DB_PASSWORD"),
        }
    }
    """
    Database settings for local development.

    :noindex:
    """

django_settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")


my_current_server = "127.0.0.1:8000"

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
"""Set ALLOWED_HOSTS to allow the server to run without a domain name for local testing."""

if "test" in sys.argv:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    """
    Specifies static files storage for testing environments.

    :noindex:
    """
