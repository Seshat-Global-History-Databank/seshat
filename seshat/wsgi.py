"""WSGI config for seshat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise


####### This is misleading, because the value that is actualyy set is 'seshat.settings.local'
# and it is probably 'production for the AWS server'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seshat.settings.base')
# if not os.path.exists(".env"):
#    os.environ["DJANGO_SETTINGS_MODULE"] = "seshat.settings.production"


application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
