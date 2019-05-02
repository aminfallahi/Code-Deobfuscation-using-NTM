from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('dynamic_scraper','0001_initial')];operations=[A.AddField(model_name='scraper',name='render_javascript',field=B.BooleanField(default=False,help_text=b'Render Javascript on pages (ScrapyJS/Splash deployment needed, careful: resource intense)'))]