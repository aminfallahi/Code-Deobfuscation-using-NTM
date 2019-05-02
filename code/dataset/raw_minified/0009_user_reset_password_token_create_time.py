from __future__ import unicode_literals
C=True
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[('account','0008_user_login_failed_counter')];operations=[A.AddField(model_name='user',name='reset_password_token_create_time',field=B.DateTimeField(null=C,blank=C))]