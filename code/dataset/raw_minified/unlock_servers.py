from django.core.management.base import BaseCommand as A
from mod.models import Server as B
class C(A):
	help='Unlocks all servers.'
	def handle(C,*D,**E):
		for A in B.objects.all():A.locked=False;A.save()