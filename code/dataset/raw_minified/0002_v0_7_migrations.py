from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('core','0001_initial')];operations=[A.AlterField(model_name='label',name='value',field=B.CharField(max_length=255,null=True,verbose_name=b'Value'))]