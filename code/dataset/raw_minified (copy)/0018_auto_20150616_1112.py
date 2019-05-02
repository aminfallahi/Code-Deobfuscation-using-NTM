from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('omaha','0017_auto_20150622_1207')];operations=[A.RunSQL('CREATE INDEX omaha_request_userid_like ON omaha_request (userid varchar_pattern_ops);',reverse_sql='Drop index omaha_request_userid_like;')]