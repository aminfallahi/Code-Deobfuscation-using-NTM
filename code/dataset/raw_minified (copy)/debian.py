__all__=['DebianServiceProvider']
from kokki.providers.service import ServiceProvider as A
class DebianServiceProvider(A):
	def enable_runlevel(A,runlevel):0