from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('base','0038_add_latest_translation')];operations=[A.AlterUniqueTogether(name='projectlocale',unique_together=set([('project','locale')]))]