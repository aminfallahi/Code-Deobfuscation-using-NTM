'Settings for testing zinnia on MySQL'
from zinnia.tests.implementations.settings import *
DATABASES={'default':{'ENGINE':'django.db.backends.mysql','NAME':'zinnia','USER':'root','HOST':'localhost'}}