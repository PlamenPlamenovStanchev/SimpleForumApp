"""
WSGI config for ForumApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ForumApp.settings')

application = get_wsgi_application()


"""
manage.py runserver

1. One instance of the project
2. Hot reloading 
3. Servers static files

gunicorn
gunicorn forumApp.wsgi:application --workers=4 --log-level=DEBUG --bind=127.0.0.1:8000


1. Specify count of workers
2. No hot reloading
3. Doesn't serve static files

"""
