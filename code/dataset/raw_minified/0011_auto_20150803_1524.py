from __future__ import unicode_literals
from django.db import migrations as A
class B(A.Migration):dependencies=[('base','0010_translation_extra')];operations=[A.AlterModelOptions(name='locale',options={'ordering':['name']})]