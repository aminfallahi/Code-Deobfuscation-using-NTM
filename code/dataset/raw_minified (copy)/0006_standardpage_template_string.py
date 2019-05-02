from __future__ import unicode_literals
C=b'pages/standard_page.html'
from django.db import migrations as A,models as B
class D(A.Migration):dependencies=[('pages','0005_auto_20151021_1630')];operations=[A.AddField(model_name='standardpage',name='template_string',field=B.CharField(default=C,max_length=255,choices=[(C,b'Default Template'),(b'pages/standard_page_full.html',b'Standard Page Full')]))]