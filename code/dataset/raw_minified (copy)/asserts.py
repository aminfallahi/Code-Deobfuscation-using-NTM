'\nsentry.testutils.asserts\n~~~~~~~~~~~~~~~~~~~~~~~~\n\n:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
from __future__ import absolute_import
def A(one,two):assert one.replace(microsecond=0)==two.replace(microsecond=0)