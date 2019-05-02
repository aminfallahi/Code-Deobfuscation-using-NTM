from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('wooey','0015_hidden_parameters')];operations=[A.AddField(model_name='wooeyfile',name='checksum',field=B.CharField(max_length=40,blank=True))]