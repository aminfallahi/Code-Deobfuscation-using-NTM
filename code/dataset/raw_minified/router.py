B=True
from django.db import DEFAULT_DB_ALIAS as A
class C:
	def __init__(B):B.db_alias=A
	def db_for_read(A,model,**B):return A.db_alias
	def db_for_write(A,model,**B):return A.db_alias
	def allow_relation(A,obj1,obj2,**C):return B
	def allow_migrate(A,db,app_label,model_name=None,**C):return B