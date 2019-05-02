from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('tests','0003_bar')];operations=[A.AddField(model_name='car',name='foos',field=B.ManyToManyField(to='tests.Foo'))]