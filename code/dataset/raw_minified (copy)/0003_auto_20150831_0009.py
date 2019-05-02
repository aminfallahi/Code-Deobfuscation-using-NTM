from __future__ import unicode_literals
from django.db import models,migrations as A
class B(A.Migration):dependencies=[('scheduling','0002_auto_20150212_0028')];operations=[A.AlterModelOptions(name='operationalslot',options={'ordering':['identifier']})]