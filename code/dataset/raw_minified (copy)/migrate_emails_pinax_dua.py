from django.conf import settings
from django.core.management.base import BaseCommand as A
from django.contrib.auth.models import User
from account.models import EmailAddress as B
class C(A):
	def handle(D,*E,**F):
		C=True
		for A in User.objects.all():B.objects.create(user=A,email=A.email,verified=C,primary=C)