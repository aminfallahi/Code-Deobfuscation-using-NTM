'\nraven.contrib.django.templatetags.raven\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n:copyright: (c) 2010-2013 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
from __future__ import absolute_import
from django import template as A
B=A.Library()
@B.simple_tag
def C(scheme=None):from raven.contrib.django.models import client as A;return A.get_public_dsn(scheme)or''