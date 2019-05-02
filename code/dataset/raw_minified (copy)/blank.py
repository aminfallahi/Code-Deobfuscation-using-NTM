C='tests.urls.simple'
from django_hosts import patterns as B,host as A
D=B('',A('',C,name='blank'),A('|www',C,name='blank_or_www'))