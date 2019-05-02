from django.core.management.base import BaseCommand as A,CommandError
from django_deploy.system import setup_server as B
from django_deploy.utils import fab_task as C
class D(A):
	@C
	def handle(self,*A,**C):B()