from __future__ import unicode_literals
from django.db import migrations as A,models
class B(A.Migration):dependencies=[('accounts','0001_initial')];operations=[A.AlterModelOptions(name='team',options={'ordering':['name']})]