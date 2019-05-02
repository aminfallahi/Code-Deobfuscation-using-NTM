from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('assets','0002_auto_20151125_1354')];operations=[A.AlterField(model_name='asset',name='force_depreciation',field=B.BooleanField(default=False,help_text='Check if you no longer want to bill for this asset'))]