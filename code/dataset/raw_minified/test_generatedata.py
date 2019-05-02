from django.core.management import call_command as A
from kitsune.sumo.tests import TestCase as B
class C(B):
	def test_generate_data(B):'Make sure ./manage.py generatedata runs.';A('generatedata')