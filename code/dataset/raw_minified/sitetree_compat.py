from django.template import Library as A
B=A()
try:from django.templatetags.future import url
except ImportError:from django.template.defaulttags import url