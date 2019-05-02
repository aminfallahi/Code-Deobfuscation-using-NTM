from __future__ import unicode_literals
B='crash'
from django.db import models,migrations as A
class C(A.Migration):dependencies=[(B,'0008_auto_20141224_0542')];operations=[A.RenameField(model_name=B,old_name='user_id',new_name='userid')]