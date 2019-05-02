from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('djangocms_forms','0002_alter_model_options')];operations=[A.AddField(model_name='formsubmission',name='referrer',field=B.CharField(max_length=150,verbose_name='Referrer URL',blank=True))]