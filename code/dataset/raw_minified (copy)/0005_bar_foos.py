from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('tests','0004_car_foos')];operations=[A.AddField(model_name='bar',name='foos',field=B.ManyToManyField(blank=True,to='tests.Foo',related_name='bars'))]