"""
WSGI config for ashrafcrowdboticscom_ud4jv_625 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ashrafcrowdboticscom_ud4jv_625.settings")

application = get_wsgi_application()
