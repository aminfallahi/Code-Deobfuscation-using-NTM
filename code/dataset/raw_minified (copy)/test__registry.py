from pyformance import MetricsRegistry as D
from pyformance.meters import Meter
from tests import TimedTestCase as A
class B(A):
	def setUp(C):super(B,C).setUp();C.registry=D(A.clock)
	def tearDown(A):super(B,A).tearDown()
	def test__add(B):B.registry.add('foo',Meter(A.clock))