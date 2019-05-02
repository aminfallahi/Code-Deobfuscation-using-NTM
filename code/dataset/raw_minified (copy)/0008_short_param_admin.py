from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('wooey','0007_script_documentation')];operations=[A.AlterField(model_name='scriptparameter',name='short_param',field=B.CharField(max_length=255,blank=True))]