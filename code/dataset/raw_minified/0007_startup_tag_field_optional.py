from __future__ import unicode_literals
from django.db import migrations as A,models as B
class C(A.Migration):dependencies=[('organizer','0006_newslink_unique_together_slug_startup')];operations=[A.AlterField(model_name='startup',name='tags',field=B.ManyToManyField(to='organizer.Tag',blank=True))]