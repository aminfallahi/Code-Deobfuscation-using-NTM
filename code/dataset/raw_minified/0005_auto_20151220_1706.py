from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('simulation','0004_auto_20151220_1640')];operations=[A.AlterModelOptions(name='passslots',options={'get_latest_by':['start']})]