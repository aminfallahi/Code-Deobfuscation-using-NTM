from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('contest','0006_merge')];operations=[A.AddField(model_name='contestsubmission',name='ac_time',field=B.IntegerField(default=0))]