'\nsentry.rules.conditions.regression_event\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
from __future__ import absolute_import
from sentry.rules.conditions.base import EventCondition as A
class B(A):
	label='An event changes state from resolved to unresolved'
	def passes(A,event,state):return state.is_regression