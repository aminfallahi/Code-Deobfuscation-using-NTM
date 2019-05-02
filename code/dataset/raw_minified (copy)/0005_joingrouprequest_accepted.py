from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('group','0004_merge')];operations=[A.AddField(model_name='joingrouprequest',name='accepted',field=B.BooleanField(default=False))]