'\nsentry.middleware.social_auth\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
from __future__ import absolute_import
from django.core.urlresolvers import reverse as A
from social_auth.middleware import SocialAuthExceptionMiddleware as B
from sentry.utils.http import absolute_uri as C
class D(B):
	def get_redirect_uri(B,request,exception):return C(A('sentry-login'))