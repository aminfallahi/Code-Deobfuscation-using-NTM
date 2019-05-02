A=True
from datetime import datetime as C
from django.db import models as B
class D(B.Model):
	pub_date=B.DateTimeField(blank=A,null=A,auto_now=A);mod_date=B.DateTimeField(blank=A,null=A,default=C.now(),editable=False)
	class Meta:abstract=A