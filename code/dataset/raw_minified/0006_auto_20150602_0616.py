from __future__ import unicode_literals
I=b'lang'
H=b'ini'
G=b'inc'
F=b'dtd'
E=b'properties'
D=b'xliff'
C=b'po'
from django.db import models as B,migrations as A
class J(A.Migration):dependencies=[('base','0005_auto_20150703_1213')];operations=[A.AlterField(model_name='resource',name='format',field=B.CharField(blank=True,max_length=20,verbose_name=b'Format',choices=[(C,C),(D,D),(E,E),(F,F),(G,G),(H,H),(I,I)]))]