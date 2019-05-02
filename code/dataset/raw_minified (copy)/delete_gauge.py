from __future__ import unicode_literals
from django.core.management.base import BaseCommand as A,CommandError as B
from redis_metrics.utils import get_r
class C(A):
	args='<gauge-key>';help='Removes a Gauge and its data'
	def handle(D,*A,**E):
		if not len(A)==1:raise B('You must provide a gauge name')
		C=get_r();C.delete_gauge(A[0])