"""
Settings for production development of the Seshat project.
"""

from .base import config

SECURE_SSL_REDIRECT = True

my_current_server = "www.majidbenam.com"

SECRET_KEY = config("SECRET_KEY")
"""
Set the secret key for the production environment.
:noindex:
"""
