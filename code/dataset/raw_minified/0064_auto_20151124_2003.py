from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('crowdsourcing','0063_auto_20151119_2242')];operations=[A.AlterField(model_name='module',name='status',field=B.IntegerField(default=3,choices=[(1,b'Draft'),(2,b'Saved'),(3,b'Published'),(4,b'Completed'),(5,b'Paused')]))]