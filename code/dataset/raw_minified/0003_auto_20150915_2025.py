from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('account','0002_user_problems_status')];operations=[A.AlterField(model_name='user',name='problems_status',field=B.TextField(default=b'{}'))]