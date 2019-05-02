from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('accounts','0004_auto_20150203_0434')];operations=[A.AlterField(model_name='myuser',name='last_login',field=B.DateTimeField(null=C,verbose_name='last login',blank=C))]