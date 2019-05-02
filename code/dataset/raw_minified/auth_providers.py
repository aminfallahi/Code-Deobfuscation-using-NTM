from __future__ import absolute_import
__all__=['AuthProvider']
from contextlib import contextmanager as A
from sentry.auth import register as B,unregister as C
@A
def AuthProvider(name,cls):B(name,cls);(yield);C(name,cls)