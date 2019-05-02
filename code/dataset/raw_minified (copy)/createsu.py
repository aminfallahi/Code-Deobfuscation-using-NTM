from django.core.management.base import BaseCommand as B
from django.contrib.auth.models import User as A
import os
class C(B):
	def handle(D,*E,**F):
		C='admin'
		if not A.objects.filter(username=C).exists():B=os.environ.get('DJANGO_ADMIN_PASSWORD');A.objects.create_superuser(C,'admin@admin.com',B)