from django.test import TestCase as A
from ..analyzers.base import Result as D,CodeSnippet as C
class B(A):
	def test_init(A):F='app/models.py';E='simple result';B=D(E,F,2);A.assertEqual(B.description,E);A.assertEqual(B.path,F);A.assertEqual(B.line,2);A.assertIsInstance(B.source,C);A.assertIsInstance(B.solution,C)