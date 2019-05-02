from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('demo_models','0003_auto_20150419_2110')];operations=[A.AddField(model_name='waiter',name='days_worked',field=B.IntegerField(default=None,null=C,blank=C))]