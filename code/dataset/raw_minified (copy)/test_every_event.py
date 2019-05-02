from __future__ import absolute_import
from sentry.testutils.cases import RuleTestCase as A
from sentry.rules.conditions.every_event import EveryEventCondition as B
class C(A):
	rule_cls=B
	def test_applies_correctly(A):B=A.get_rule();A.assertPasses(B,A.event,is_new=True);A.assertPasses(B,A.event,is_new=False)