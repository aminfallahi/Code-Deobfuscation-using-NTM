import os
from django.test import TestCase as A
from mock import patch
class B(A):
	@patch.dict(os.environ,clear=True,DJANGO_CONFIGURATION='DotEnvConfiguration',DJANGO_SETTINGS_MODULE='tests.settings.dot_env')
	def test_env_loaded(self):from tests.settings import dot_env as A;self.assertEqual(A.DOTENV_VALUE,'is set');self.assertEqual(A.DOTENV_LOADED,A.DOTENV)