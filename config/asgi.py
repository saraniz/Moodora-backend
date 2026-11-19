"""
ASGI config for config project.

ASGI (Asynchronous Server Gateway Interface) is the standard that lets
async-capable web servers (like Daphne or Uvicorn) talk to Django.
It is used for modern features like WebSockets and background tasks.

It exposes the ASGI callable as a module-level variable named ``application``.
Web servers look for this `application` object to start running your Django project.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os            # Lets us read and set environment variables

# Import Django's helper that creates the ASGI application object.
from django.core.asgi import get_asgi_application

# Tell Django which settings file to use.
# setdefault means "only set this if it isn't already set".
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# `application` is the ASGI callable. A web server imports this object
# and calls it for every incoming web request.
application = get_asgi_application()
