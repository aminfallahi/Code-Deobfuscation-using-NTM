from __future__ import unicode_literals
from django.db import migrations as A,models
class B(A.Migration):dependencies=[('blog','0003_post_fields_startups_and_tags_optional')];operations=[A.AlterModelOptions(name='post',options={'ordering':['-pub_date','title'],'verbose_name':'blog post','get_latest_by':'pub_date','permissions':(('view_future_post','Can view unpublished Post'),)})]