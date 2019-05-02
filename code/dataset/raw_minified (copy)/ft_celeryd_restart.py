from django.core.management.base import BaseCommand as A,CommandError as B
class C(A):
	help='Restarts all celery daemons.'
	def handle(C,*D,**E):
		try:from celery.task.control import broadcast as A
		except ImportError:raise B('Celery is not currently installed.')
		A('shutdown')