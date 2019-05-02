from __future__ import unicode_literals
from django.core.management.base import BaseCommand as A
from ...models import Customer as B
from ...settings import get_subscriber_model as C
class D(A):
	help="Create customer objects for existing subscribers that don't have one"
	def handle(D,*E,**F):
		for A in C().objects.filter(customer__isnull=True):B.get_or_create(subscriber=A);print('Created subscriber for {0}'.format(A.email))