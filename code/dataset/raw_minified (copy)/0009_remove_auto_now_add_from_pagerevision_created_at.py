from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('wagtailcore','0008_populate_latest_revision_created_at')];operations=[A.AlterField(model_name='pagerevision',name='created_at',field=B.DateTimeField())]