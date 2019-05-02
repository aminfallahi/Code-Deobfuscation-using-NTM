from utils.management.commands.base.db_procedure_command import DBProcedureCommand as A
import logging as B
class C(A):help='Updates hits_mv.hits_posted related to initial group posts which  are ommitted by the regular hits_update.';proc_name='initial_post_hits_update';logger=B.getLogger('mturk.arrivals.db_initial_post_hits_update')