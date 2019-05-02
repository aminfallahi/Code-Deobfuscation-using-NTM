from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('wooey','0006_script_group_defaults')];operations=[A.AddField(model_name='script',name='documentation',field=B.TextField(null=C,blank=C))]