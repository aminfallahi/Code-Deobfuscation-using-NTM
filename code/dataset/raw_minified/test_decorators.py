C='scenario/decorators'
from nose2.tests._common import FunctionalTestCase as A
class B(A):
	def test_with_setup(A):B=A.runIn(C,'test_decorators.test_with_setup');A.assertTestRunOutputMatches(B,stderr='Ran 1 test');A.assertEqual(B.poll(),0,B.stderr.getvalue())
	def test_with_teardown(A):B=A.runIn(C,'test_decorators.test_with_teardown','test_decorators.test_teardown_ran');A.assertTestRunOutputMatches(B,stderr='Ran 2 test');A.assertEqual(B.poll(),0,B.stderr.getvalue())