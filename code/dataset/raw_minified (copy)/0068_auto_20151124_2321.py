from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('crowdsourcing','0067_auto_20151124_2302')];operations=[A.AlterField(model_name='project',name='keywords',field=B.TextField(null=C,blank=C))]