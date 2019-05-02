from __future__ import unicode_literals
C=True
from django.db import migrations as A,models as B
class D(A.Migration):dependencies=[('users','0011_add_csat_email_sent_field')];operations=[A.AlterField(model_name='emailchange',name='email',field=B.EmailField(max_length=254,null=C,db_index=C))]