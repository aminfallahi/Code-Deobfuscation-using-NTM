from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('scheduling','0007_auto_20150904_0733')];operations=[A.RemoveField(model_name='operationalslot',name='compatible_channels')]