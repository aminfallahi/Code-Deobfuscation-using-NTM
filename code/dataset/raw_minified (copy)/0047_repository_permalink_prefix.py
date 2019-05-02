from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('base','0046_add_force_suggestions')];operations=[A.AddField(model_name='repository',name='permalink_prefix',field=B.CharField(max_length=2000,verbose_name=b'Permalink prefix',blank=True))]