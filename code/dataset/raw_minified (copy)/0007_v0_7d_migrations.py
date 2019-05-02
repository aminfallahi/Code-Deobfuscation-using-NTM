from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('cloud','0006_v0_7c_migrations')];operations=[A.AddField(model_name='cloudaccount',name='create_security_groups',field=B.BooleanField(default=True,verbose_name=b'Create Security Groups'))]