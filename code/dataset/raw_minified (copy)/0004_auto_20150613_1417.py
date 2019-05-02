from __future__ import unicode_literals
C='ladder'
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[(C,'0003_auto_20140910_1838')];operations=[A.AlterField(model_name=C,name='division',field=B.IntegerField(max_length=11))]