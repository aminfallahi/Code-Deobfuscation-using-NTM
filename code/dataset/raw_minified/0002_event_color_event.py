from __future__ import unicode_literals
C=True
from django.db import migrations as A,models as B
class D(A.Migration):dependencies=[('schedule','0001_initial')];operations=[A.AddField(model_name='event',name='color_event',field=B.CharField(verbose_name='Color event',blank=C,max_length=10,null=C))]