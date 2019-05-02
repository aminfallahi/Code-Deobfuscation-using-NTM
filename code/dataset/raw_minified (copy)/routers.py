C='djangodblog'
from djangodblog import settings as A
class B:
	def db_for_write(B,model,**D):
		if model._meta.app_label==C:return A.DATABASE_USING
	def db_for_read(A,model,**B):return A.db_for_write(model,**B)
	def allow_syncdb(D,db,model):
		B=A.DATABASE_USING
		if not B:return None
		if model._meta.app_label==C and db!=B:return False