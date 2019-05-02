from django.db import models as A
class B(A.Model):
	spam_flag=A.ManyToManyField('SpammyPosting')
	class Meta:abstract=True