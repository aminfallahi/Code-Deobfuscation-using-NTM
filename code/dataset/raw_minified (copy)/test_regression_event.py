from __future__ import absolute_import
from sentry.testutils.cases import RuleTestCase as A
from sentry.rules.conditions.regression_event import RegressionEventCondition as B
class C(A):
	rule_cls=B
	def test_applies_correctly(A):B=A.get_rule();A.assertPasses(B,A.event,is_regression=True);A.assertDoesNotPass(B,A.event,is_regression=False)