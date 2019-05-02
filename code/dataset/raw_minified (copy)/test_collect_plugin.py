from nose2.tests._common import FakeStartTestRunEvent as C,TestCase as A
from nose2.plugins import collect as B
from nose2 import session as D
class E(A):
	tags=['unit']
	def setUp(A):A.session=D.Session();A.plugin=B.CollectOnly(session=A.session)
	def test_startTestRun_sets_executeTests(A):B=C();A.plugin.startTestRun(B);A.assertEqual(B.executeTests,A.plugin.collectTests)