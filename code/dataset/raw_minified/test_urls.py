'\n\nThis is a urlconf to be loaded by tests.py. Add any urls needed\nfor tests only.\n\n'
from django.conf.urls.defaults import *
from django.contrib.formtools.tests import *
urlpatterns=patterns('',('^test1/',TestFormPreview(TestForm)))