from django.core.management.base import NoArgsCommand as A
import kronos as B
@B.register('0 0 * * *',args={})
class C(A):
	help='Register tasks with cron'
	def handle_noargs(A,**B):print('command task')