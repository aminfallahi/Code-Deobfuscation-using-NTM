import unittest as A
class B(A.TestCase):
	def setUp(A):0
	def test_unconfigured_engine(A):
		'Raise an exception when the db engine is not configured'
		try:from pybald.context import models as B;B.engine.execute('SELECT 1234')
		except RuntimeError as C:pass
		else:A.fail('Runtime exception not thrown')