from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('base','0035_remove_deleted_field')];operations=[A.AddField(model_name='project',name='has_changed',field=B.BooleanField(default=False))]