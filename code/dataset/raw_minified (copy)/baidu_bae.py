import os,sys
os.environ['DJANGO_SETTINGS_MODULE']='settings'
A=os.path.dirname(os.path.abspath(__file__))+'./'
if A not in sys.path:sys.path.insert(1,A)
from django.core.handlers.wsgi import WSGIHandler as B
from bae.core.wsgi import WSGIApplication as C
D=C(B())