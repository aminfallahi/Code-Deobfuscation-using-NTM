from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('metrics','0001_initial')];operations=[A.RenameField(model_name='metric',old_name='select',new_name='query')]