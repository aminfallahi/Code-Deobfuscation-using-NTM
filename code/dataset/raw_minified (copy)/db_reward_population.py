from utils.management.commands.base.db_procedure_command import DBProcedureCommand as A
import logging as B
class C(A):help='Populates crawagrefates hits_posted and hits_consumed based on hits_mv records.';proc_name='reward_population';logger=B.getLogger('mturk.arrivals.db_reward_population')