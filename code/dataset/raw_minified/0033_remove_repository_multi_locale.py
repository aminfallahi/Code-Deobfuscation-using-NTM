from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('base','0032_repository_last_synced_revisions')];operations=[A.RemoveField(model_name='repository',name='multi_locale')]