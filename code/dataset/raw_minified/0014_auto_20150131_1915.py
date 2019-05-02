from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('videos','0013_auto_20150130_2131')];operations=[A.AlterModelOptions(name='video',options={'ordering':['order','-timestamp']})]