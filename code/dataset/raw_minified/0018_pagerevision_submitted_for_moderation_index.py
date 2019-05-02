from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('wagtailcore','0017_change_edit_page_permission_description')];operations=[A.AlterField(model_name='pagerevision',name='submitted_for_moderation',field=B.BooleanField(default=False,db_index=True,verbose_name='Submitted for moderation'))]