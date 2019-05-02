from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('users','0002_v0_7_migrations')];operations=[A.AddField(model_name='usersettings',name='advanced_view',field=B.BooleanField(default=False,verbose_name=b'Advanced View'))]