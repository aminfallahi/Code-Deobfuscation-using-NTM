import django as A
if A.VERSION>=(1,5):import json
else:from django.utils import simplejson as json