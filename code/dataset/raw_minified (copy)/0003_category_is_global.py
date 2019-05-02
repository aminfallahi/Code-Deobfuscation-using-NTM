from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('spirit_category','0002_auto_20150728_0442')];operations=[A.AddField(model_name='category',name='is_global',field=B.BooleanField(default=True,help_text='Designates whether the topics will bedisplayed in the all-categories list.',verbose_name='global'))]