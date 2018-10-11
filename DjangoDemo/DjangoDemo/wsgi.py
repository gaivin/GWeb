"""
WSGI config for DjangoDemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
path = '/home/gaivin/DjangoDemo'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoDemo.settings'
#
## then, for django >=1.5:
application = get_wsgi_application()
## or, for older django <=1.4
# import django.core.handlers.wsgi
# application = django.core.handlers.wsgi.WSGIHandler()
