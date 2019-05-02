from django.core.management.base import BaseCommand as A
from denorm import denorms as B
class C(A):
	help='Recalculates the value of every denormalized field that was marked dirty.'
	def handle(A,**C):B.flush()