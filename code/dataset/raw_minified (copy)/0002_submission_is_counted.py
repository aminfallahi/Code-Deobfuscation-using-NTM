from __future__ import unicode_literals
C='submission'
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[(C,'0001_initial')];operations=[A.AddField(model_name=C,name='is_counted',field=B.BooleanField(default=False))]