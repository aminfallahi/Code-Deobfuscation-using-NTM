from __future__ import print_function
from providers.provider import BaseProvider as A
class B(A):
	IDENTIFIER=None
	def output(A,movie_data):raise NotImplementedError('Subclasses must implement output')