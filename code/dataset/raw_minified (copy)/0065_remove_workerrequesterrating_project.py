from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('crowdsourcing','0064_merge')];operations=[A.RemoveField(model_name='workerrequesterrating',name='project')]