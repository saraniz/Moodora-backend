#!/usr/bin/env python
# This file is Django's command-line utility. It lets you run Django admin
# commands like `python manage.py runserver`, `python manage.py migrate`, etc.
# You run it from the terminal to manage your project.
"""Django's command-line utility for administrative tasks."""
import os          # Lets us read and set environment variables
import sys         # Lets us read command-line arguments you typed


def main():
    # This function runs when you execute this file.
    # It sets up Django and then runs whatever admin command you asked for.
    """Run administrative tasks."""
    # Tell Django which settings file to use (config/settings.py).
    # setdefault means "only set this if it isn't already set".
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Import Django's command runner.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django isn't installed, show a helpful error message.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Run the command you typed (e.g. runserver, migrate, createsuperuser).
    execute_from_command_line(sys.argv)


# This block only runs when you run this file directly (not when imported).
# __name__ is '__main__' when the file is executed as a script.
if __name__ == '__main__':
    main()
