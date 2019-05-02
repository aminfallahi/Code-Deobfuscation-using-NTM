from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('cmsplugin_contact_plus','0001_initial')];operations=[A.AlterField(model_name='contactplus',name='recipient_email',field=B.EmailField(default=b'',max_length=254,verbose_name='Email of recipients'))]