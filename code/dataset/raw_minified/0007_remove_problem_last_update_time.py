from __future__ import unicode_literals
B='problem'
from django.db import models,migrations as A
class C(A.Migration):dependencies=[(B,'0006_merge')];operations=[A.RemoveField(model_name=B,name='last_update_time')]