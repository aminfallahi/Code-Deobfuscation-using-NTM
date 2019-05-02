from __future__ import absolute_import
from django.core.urlresolvers import reverse as C
from sentry.testutils import TestCase as A
class B(A):
	urls='sentry.conf.urls'
	def test_simple(A):D=C('error-403-csrf-failure');B=A.client.get(D);assert B.status_code==403;A.assertTemplateUsed(B,'sentry/403-csrf-failure.html')