from django.core.management.base import BaseCommand as A
from olympia.addons.models import Addon
from olympia.amo.utils import chunked as B
from olympia.amo.tasks import dedupe_approvals as C
class D(A):
	help='Dedupes activity for addon approvals log'
	def handle(E,*F,**G):
		A=Addon.objects.values_list('pk',flat=True).order_by('id')
		for D in B(A,100):C.delay(D)