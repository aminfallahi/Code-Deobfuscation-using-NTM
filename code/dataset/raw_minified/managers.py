from django.db import models as A
from django.db.models.query import QuerySet as B
class C(B):
	def active(A):'\n        Return only "active" (i.e. published) questions.\n        ';return A.filter(status__exact=A.model.ACTIVE)
class D(A.Manager):
	def get_query_set(A):return C(A.model)
	def active(A):return A.get_query_set().active()