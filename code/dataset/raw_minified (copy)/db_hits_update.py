from utils.management.commands.base.db_procedure_command import DBProcedureCommand as A
import logging as B
class C(A):help='Updates hits_mv hits_posted and hits_consumed using date from hits_temp.';proc_name='hits_update';logger=B.getLogger('mturk.arrivals.db_hits_update')