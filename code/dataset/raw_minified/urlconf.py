'ImportD import helper.'
try:from django.conf.urls import patterns
except ImportError:from django.conf.urls.defaults import patterns
finally:A=patterns('')