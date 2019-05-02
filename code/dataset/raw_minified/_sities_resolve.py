C=None
from ..  import utils as A
try:
	from django_jinja import library as B
	@B.global_function
	def D(name,*D,**B):E=B.pop('site_id',C);return A.reverse(name,args=D,kwargs=B,site_id=E)
	@B.global_function
	def E(path,site_id=C):return A.static(path,site_id=site_id)
except ImportError:pass