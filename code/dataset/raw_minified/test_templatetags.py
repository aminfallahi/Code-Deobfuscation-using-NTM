from django.template import Context as B,Template as C
from .base import watch,TestCase as A
class D(A):
	'Tests for our lone template tag'
	def test_unsubscribe_instructions(E):'Make sure unsubscribe_instructions renders and contains the\n        unsubscribe URL.';A=watch(save=True);D=C('{% load unsubscribe_instructions %}{% unsubscribe_instructions watch %}');assert A.unsubscribe_url()in D.render(B({'watch':A}))