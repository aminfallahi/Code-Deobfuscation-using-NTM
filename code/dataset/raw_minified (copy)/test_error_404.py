from __future__ import absolute_import
from django.core.urlresolvers import reverse as C
from sentry.testutils import TestCase as A
class B(A):
	urls='sentry.conf.urls'
	def test_renders(A):B=A.client.get(C('error-404'));assert B.status_code==404;A.assertTemplateUsed(B,'sentry/404.html')