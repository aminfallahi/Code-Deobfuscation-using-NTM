from django.conf import settings as B
from omblog import settings as C
def A(key):
	try:A=B.CACHES['default']['KEY_PREFIX']
	except KeyError:A=''
	return'%s_%s_%s'%(A,C.CACHE_PREFIX,key)