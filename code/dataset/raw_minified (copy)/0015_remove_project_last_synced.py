from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('base','0014_auto_20150806_0948')];operations=[A.RemoveField(model_name='project',name='last_synced')]