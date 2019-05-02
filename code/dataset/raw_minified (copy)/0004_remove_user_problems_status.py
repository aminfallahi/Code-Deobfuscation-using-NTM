from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('account','0003_auto_20150915_2025')];operations=[A.RemoveField(model_name='user',name='problems_status')]