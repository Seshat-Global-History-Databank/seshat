#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    local_env_path = str(Path.cwd()) + "/seshat/settings/.env"
    if os.path.exists(local_env_path):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'seshat.settings.local')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'seshat.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
