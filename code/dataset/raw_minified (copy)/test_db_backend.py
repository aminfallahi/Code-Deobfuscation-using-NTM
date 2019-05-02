from __future__ import absolute_import,unicode_literals
import unittest as A
from django.test import TestCase as C
from .test_backends import BackendTests as D
class B(D,C):
	backend_path='wagtail.wagtailsearch.backends.db'
	@A.expectedFailure
	def test_callable_indexed_field(self):super(B,self).test_callable_indexed_field()
	@A.expectedFailure
	def test_update_index_command(self):super(B,self).test_update_index_command()