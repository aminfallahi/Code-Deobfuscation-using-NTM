from __future__ import absolute_import,print_function
from sentry.tasks.base import instrumented_task as A
from sentry.lang.native.dsymcache import dsymcache as B
@A(name='sentry.tasks.clear_old_cached_dsyms',time_limit=15,soft_time_limit=10)
def C():B.clear_old_entries()