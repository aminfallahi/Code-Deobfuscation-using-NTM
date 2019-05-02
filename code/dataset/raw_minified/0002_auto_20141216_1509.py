from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('reversion','0001_initial')];operations=[A.AlterField(model_name='revision',name='manager_slug',field=B.CharField(default='default',max_length=191,db_index=True))]