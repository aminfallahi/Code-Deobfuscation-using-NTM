from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('crowdsourcing','0071_merge')];operations=[A.AddField(model_name='module',name='template',field=B.ManyToManyField(to='crowdsourcing.Template',through='crowdsourcing.ModuleTemplate'))]