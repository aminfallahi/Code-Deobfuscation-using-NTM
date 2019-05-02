C=None
from django.conf import settings as A
class B:
	@staticmethod
	def in_postgres(model):A=model;B=A._meta.app_label;C=A._meta.model_name;return B=='cachalot'and C=='postgresmodel'
	def get_postgresql_alias(C):B='postgresql';return B if B in A.DATABASES else'default'
	def allow_migrate(A,db,app_label,model=C,**D):
		B=model
		if D.get('extension')in('hstore','unaccent')or B is not C and A.in_postgres(B):return db==A.get_postgresql_alias()