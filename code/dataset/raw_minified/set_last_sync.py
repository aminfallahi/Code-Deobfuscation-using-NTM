import redis
from django.conf import settings as A
from django.core.management.base import BaseCommand as B
class C(B):
	def handle(D,*B,**E):
		C=redis.StrictRedis(**dict([(B.lower(),C)for(B,C)in A.REDIS[A.PYPI_DATASTORE].items()]))
		if B:C.set('crate:pypi:since',B[0])