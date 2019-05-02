import unittest as A
class B(A.TestCase):
	def test_it(B):
		from ..  import subscribers as A
		def C(value):B.assertEqual(value,'started')
		try:D=A.statsd_incr;A.statsd_incr=C;A.on_startup(None)
		finally:A.statsd_incr=D