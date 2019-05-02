from __future__ import unicode_literals
from django.db import migrations as A,models
class B(A.Migration):dependencies=[('organizer','0005_newslink_slug')];operations=[A.AlterUniqueTogether(name='newslink',unique_together=set([('slug','startup')]))]