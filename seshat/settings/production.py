"""
Settings for production development of the Seshat project.
"""

from .base import config

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

SEURE_SSL_REDIRECT = True

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

my_current_server = "www.majidbenam.com"


# Secret Key
SECRET_KEY = config("SECRET_KEY")
"""
Set the secret key for the production environment.
:noindex:
"""
