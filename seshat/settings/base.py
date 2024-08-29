"""
The base settings for the Seshat project.

They are used by the development and production environment settings,
available in :doc:`/api/seshat/settings/local/index` and
:doc:`/api/seshat/settings/production/index`.
"""

from django.contrib.messages import constants as messages

import os
import django_heroku
import sys

from pathlib import Path

from decouple import config

# TODO: define __all__ for this module


MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

local_env_path = str(Path.cwd()) + "/seshat/settings/.env"

# BASE_DIR is calculated based on this file (base.py) and then goes to parents above.
BASE_DIR = Path(__file__).resolve().parent.parent

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config("SECRET_KEY", default="django-insecure$seshat.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

if DEBUG:
    MY_CURRENT_SERVER = "http://127.0.0.1:8000"
else:
    MY_CURRENT_SERVER = "https://www.majidbenam.com"

ALLOWED_HOSTS = [
    "seshatdb.herokuapp.com",
    "127.0.0.1",
    "majidbenam.com",
    "www.majidbenam.com",
    "https://majidbenam.com",
]


INSTALLED_APPS = [
    "seshat.apps.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Add this
    "django.contrib.humanize",
    "crispy_forms",
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
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
    #'allauth.socialaccount.auth_backends.AuthenticationBackend',
]

if not os.path.exists(local_env_path) and not os.getenv("GITHUB_ACTIONS") == "true":
    RECAPTCHA_PUBLIC_KEY = config("GOOGLE_RECAPTCHA_SITE_KEY")
    RECAPTCHA_PRIVATE_KEY = config("GOOGLE_RECAPTCHA_SECRET_KEY")
    INSTALLED_APPS.append("django_recaptcha")

# all-auth
LOGIN_REDIRECT_URL = "seshat-index"
ACCOUNT_LOGOUT_REDIRECT = "seshat-index"
SITE_ID = 2
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[Django Seshat] '  # Customize email subjects
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

# SOCIALACCOUNT_AUTO_SIGNUP = False

if not os.path.exists(local_env_path) and not os.getenv("GITHUB_ACTIONS") == "true":
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
    """SOCIALACCOUNT_PROVIDERS defines the social account providers for the Django all-auth package."""

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
"""DEFAULT_AUTO_FIELD is set to `django.db.models.BigAutoField`."""

# ROOT_URLCONF = "urls"
ROOT_URLCONF = "seshat.urls"
"""ROOT_URLCONF is set to the URL configuration for the Seshat project."""

INTERNAL_IPS = ["127.0.0.1"]
"""INTERNAL_IPS defines the list of IP addresses that are allowed to visit the debug toolbar."""

WSGI_APPLICATION = "seshat.wsgi.application"
"""WSGI_APPLICATION is set to the WSGI application for the Seshat project."""

# AUTH_USER_MODEL = 'accounts.CustomUser'

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "easyaudit.middleware.easyaudit.EasyAuditMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]
"""MIDDLEWARE defines the list of middleware classes that Django will use."""

# DJANGO_EASY_AUDIT_REGISTERED_CLASSES = ['sc.script']

# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

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
                "seshat.apps.core.context_processors.notifications",  # Add your context processor
            ],
        },
    },
]
"""TEMPLATES defines the list of engines that Django can use to render templates."""


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)

# Qing data database
if not os.path.exists(local_env_path) and not os.getenv("GITHUB_ACTIONS") == "true":
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

# DATABASES['default'] = dj_database_url.config(conn_max_age=600)

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
"""

CSRF_TRUSTED_ORIGINS = [
    "https://majidbenam.com",
    "http://*.majidbenam.com",
    "http://majidbenam.com",
    "https://seshatdb.herokuapp.com",
    "http://seshatdb.herokuapp.com",
    "https://*.majidbenam.com",
]  # the most important one is the last one.
"""CSRF_TRUSTED_ORIGINS defines the trusted origins for Cross-Site Request Forgery (CSRF) protection."""
# USE_X_FORWARDED_HOST = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

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
"""LOCALE_PATHS defines the directories in which Django will search for translation files."""

# Email config BACKUP:
if not os.path.exists(local_env_path) and not os.getenv("GITHUB_ACTIONS") == "true":
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

######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'xxxx.xxx@gmail.com'
# EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

# STATIC_URL = "/static/"
# this is all browser stuff, what  you need to type in the address bar to see the image and stuff
STATIC_URL = "static/"
"""
The URL to use when referring to static files located in the `static` directory.
"""

# this is not needed: the actual value is the default valu:
# /home/majid/dev/seshat/seshat/seshat/staticfiles
# and the files are actually stored there when we COLLECTSTATIC them
STATIC_ROOT = BASE_DIR.parent.parent / "static"
"""
The absolute path to the directory where `collectstatic` will collect static files for deployment.

Note:
    The value set here is the `static` directory in the base directory of the project.
"""

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# This one is pretty pointless too but let's keep things as it is for the moment
# I believe this says: anything under the base directory that is inside a directory
# called 'static' will be collected as staticfile, egardless of how deep down in
# the directory hierarchy it might be. It just needs to be a in a older called media
# in any of the apps, etc.
STATICFILES_DIRS = [BASE_DIR / "static"]
"""
Defines the directories in which Django will search for additional static files.
"""


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
"""
The static files storage is set to the whitenoise storage, which is a compressed
manifest static files storage.
"""

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
if "test" in sys.argv:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    """
    The static files storage is set to the Django static files storage for testing
    environments.

    :noindex:
    """

# We might need to turn these on in production!
# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# )


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"
"""The URL to use when referring to media files located in the `media` directory."""

MEDIA_ROOT = BASE_DIR.parent.parent / "media"
"""The absolute path to the directory where uploaded files will be saved."""


# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

SESHAT_ENVIRONMENT = config("SESHAT_ENVIRONMENT", default="local")
"""
The environment in which the Seshat application is running.

Note:
    The value is set to `local` by default. This value can be changed in the
    environment variable SESHAT_ENVIRONMENT.
"""

# =================
# Login Redirect
# =================

# LOGIN_REDIRECT_URL = 'seshat-index'  # (see L100 above)


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
"""CORS_ALLOWED_ORIGINS defines the allowed origins for Cross-Origin Resource Sharing (CORS)."""

# =================
# Logout Redirect
# =================
# LOGOUT_REDIRECT_URL = 'logout'

# I believe this says: Hey Heroku, do your local settings, don't care about my static_root, static_url etc.
django_heroku.settings(locals())

# Geospatial stuff: modify the paths to the libraries for your system setup
GEOGRAPHIC_DB = True
"""GEOGRAPHIC_DB is set to True to enable the geographic database."""

if sys.platform.startswith("darwin"):
    # macOS settings
    GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
    GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"
else:
    # Linux settings
    if os.getenv("GITHUB_ACTIONS") == "true":
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
