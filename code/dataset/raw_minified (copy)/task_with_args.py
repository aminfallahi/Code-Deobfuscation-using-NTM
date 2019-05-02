from django.core.management.base import NoArgsCommand as A
import kronos as B
@B.register('0 0 * * *',args={'--arg1':None,'-b':'some-arg2','--some-list':['site1','site2','site3']})
class C(A):
	help='Register tasks with cron'
	def handle_noargs(A,**B):print('command task')