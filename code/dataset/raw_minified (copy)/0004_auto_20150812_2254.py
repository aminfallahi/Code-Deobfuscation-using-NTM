from __future__ import unicode_literals
C='problem'
from django.db import models as B,migrations as A
class D(A.Migration):dependencies=[(C,'0003_auto_20150810_2233')];operations=[A.AlterField(model_name=C,name='tags',field=B.ManyToManyField(to='problem.ProblemTag'))]