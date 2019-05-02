from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('membership','0003_ensure_http_prefix_contact_uris')];operations=[A.AlterField(model_name='contact',name='phone',field=B.CharField(max_length=64,verbose_name='Phone',blank=True))]