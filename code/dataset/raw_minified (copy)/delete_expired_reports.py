from django.conf import settings
from django.core.management.base import BaseCommand as A
from lint.models import Report as B
class C(A):
	help='Deletes expired reports'
	def handle(A,*C,**D):B.objects.delete_expired()