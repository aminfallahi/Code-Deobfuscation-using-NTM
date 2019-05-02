from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('pro','0001_initial')];operations=[A.AlterField(model_name='paypalnvp',name='ipaddress',field=B.GenericIPAddressField(null=C,blank=C))]