#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproyecto_9.settings')

=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproyecto_10.settings')
>>>>>>> c22b6f0025b2cd0140e33110c1f0a319f12b12ba

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
