from subprocess import call
from django.core.management.base import BaseCommand as A
class B(A):
	help="Restarts one or all of supervisord's managed programs"
	def handle(A,*C,**D):
		A.args=C;A.options=D;B=['supervisorctl','restart']
		if A.args:B+=A.args
		else:B.append('all')
		call(B)