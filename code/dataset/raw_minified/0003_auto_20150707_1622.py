from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('metrics','0002_auto_20150703_0937')];operations=[A.RenameField(model_name='metricvalue',old_name='settings',new_name='metric')]