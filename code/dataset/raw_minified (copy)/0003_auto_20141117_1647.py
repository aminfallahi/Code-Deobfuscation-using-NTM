from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('ipn','0002_paypalipn_mp_id')];operations=[A.AlterField(model_name='paypalipn',name='ipaddress',field=B.GenericIPAddressField(null=C,blank=C))]