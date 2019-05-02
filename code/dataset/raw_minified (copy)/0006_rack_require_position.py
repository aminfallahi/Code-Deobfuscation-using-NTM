from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('data_center','0005_auto_20160121_1133')];operations=[A.AddField(model_name='rack',name='require_position',field=B.BooleanField(default=True,help_text='Uncheck if position is optional for this rack (ex. when rack has warehouse-kind role'))]