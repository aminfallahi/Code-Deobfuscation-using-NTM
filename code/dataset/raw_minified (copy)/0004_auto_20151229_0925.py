from __future__ import unicode_literals
from django.db import migrations as A,models
class B(A.Migration):dependencies=[('supports','0003_auto_20151204_1325')];operations=[A.AlterUniqueTogether(name='BaseObjectsSupport',unique_together=set([('support','baseobject')]))]