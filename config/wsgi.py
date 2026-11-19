"""
WSGI config for config project.

WSGI (Web Server Gateway Interface) is the standard that lets
traditional web servers (like Gunicorn or uWSGI) talk to Django.
It is used for regular HTTP request/response handling.

It exposes the WSGI callable as a module-level variable named ``application``.
Web servers look for this `application` object to start running your Django project.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os            # Lets us read and set environment variables

# Import Django's helper that creates the WSGI application object.
from django.core.wsgi import get_wsgi_application

# Tell Django which settings file to use.
# setdefault means "only set this if it isn't already set".
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# `application` is the WSGI callable. A web server imports this object
# and calls it for every incoming web request.
application = get_wsgi_application()
