from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('base','0023_auto_20150916_0642')];operations=[A.AddField(model_name='locale',name='team_description',field=B.TextField(blank=True))]