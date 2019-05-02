from __future__ import unicode_literals
from django.db import models as B,migrations as A
class C(A.Migration):dependencies=[('django_easy_currencies','0001_initial')];operations=[A.AlterField(model_name='currencyrate',name='rate',field=B.DecimalField(max_digits=13,decimal_places=9))]