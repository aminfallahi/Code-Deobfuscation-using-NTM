C='0 0 * * *'
B=print
import kronos as A
@A.register(C)
def D():B('Kronos makes it really easy to define and schedule tasks with cron!')
@A.register(C,args={'--arg1':None,'-b':'some-arg2','--some-list':['site1','site2','site3']})
def E():B('Kronos makes it really easy to define and schedule tasks with cron, even with arguments!')
@A.register(C,args={})
def F():B('Kronos makes it really easy to define and schedule tasks with cron, even with arguments, that you can forget and it still work!')