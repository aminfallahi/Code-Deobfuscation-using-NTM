from __future__ import absolute_import,unicode_literals
from .base import *
DEBUG=True
SECRET_KEY='{{ secret_key }}'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
try:from .local import *
except ImportError:pass