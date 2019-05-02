from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('helpdesk','0006_email_maxlength')];operations=[A.AlterField(model_name='customfield',name='label',field=B.CharField(help_text='The display label for this field',max_length=30,verbose_name='Label'))]