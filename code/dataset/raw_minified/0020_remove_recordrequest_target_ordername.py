from __future__ import unicode_literals
from django.db import migrations as A,models
class B(A.Migration):dependencies=[('powerdns','0019_auto_20160111_0842')];operations=[A.RemoveField(model_name='recordrequest',name='target_ordername')]