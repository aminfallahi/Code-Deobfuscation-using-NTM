from __future__ import absolute_import
from sentry.models import Counter as B
from sentry.testutils import TestCase as A
class C(A):
	def test_increment(A):D=A.create_user();E=A.create_organization(owner=D);F=A.create_team(organization=E);C=A.create_project(team=F);assert B.increment(C,42)==42;assert B.increment(C,1)==43