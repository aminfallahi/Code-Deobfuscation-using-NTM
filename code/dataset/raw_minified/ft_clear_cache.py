from django.core.management.base import BaseCommand as A
from django.core.cache import cache
class B(A):
	help='Flushes the Django cache.'
	def handle(A,*B,**C):cache.clear()