from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('crowdsourcing','0068_userpreferences_auto_skip')];operations=[A.RenameField(model_name='userpreferences',old_name='auto_skip',new_name='auto_accept')]