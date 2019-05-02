from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('djangocms_forms','0003_add_referrer_field')];operations=[A.AddField(model_name='formdefinition',name='redirect_delay',field=B.PositiveIntegerField(verbose_name='Redirect Delay',blank=C,null=C,help_text='Wait this number of milliseconds before redirecting.'))]