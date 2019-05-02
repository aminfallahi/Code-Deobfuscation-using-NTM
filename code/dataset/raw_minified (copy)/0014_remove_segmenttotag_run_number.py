from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('corpus','0013_auto_20141014_2136')];operations=[A.RemoveField(model_name='segmenttotag',name='run_number')]