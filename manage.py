#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproyecto_10.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproyecto_8.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproyecto_7.settings')
>>>>>>> ad69e919bf074e80db8b865022a0382959a50a56
>>>>>>> fd9b4414b63cf528b1b6d4b4638af6fa8db2725f
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
