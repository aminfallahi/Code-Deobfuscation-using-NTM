from django.core.management.base import NoArgsCommand as A
from kronos import uninstall as B
class C(A):
	help='Remove tasks from cron'
	def handle_noargs(C,**D):A=B();print('{} tasks removed'.format(A))