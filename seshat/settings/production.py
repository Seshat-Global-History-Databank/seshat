"""
Settings for production development of the Seshat project.
"""

# flake8: noqa

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

import seshat
from .base import *

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True

# SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SEURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# SESSION_COOKIE_SECURE = True

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

my_current_server = "www.majidbenam.com"


# sentry_sdk.init(
#     dsn=config("SENTRY_DSN", default=""),
#     environment=SESHAT_ENVIRONMENT,
#     release="seshat@%s" % seshat.__version__,
#     integrations=[DjangoIntegration()],
# )

# Secret Key
SECRET_KEY = config('SECRET_KEY')
"""
Set the secret key for the production environment.
:noindex:
"""
