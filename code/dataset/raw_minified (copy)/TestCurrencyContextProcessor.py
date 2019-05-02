from __future__ import unicode_literals
from django.test.testcases import TestCase as A
class B(A):
	def test_processor_sets_expected_variables_in_context(A):B=A.client.get('/');A.assertEqual(B.context['active_currency'],'USD');A.assertIsInstance(B.context['currency_rates'],dict)