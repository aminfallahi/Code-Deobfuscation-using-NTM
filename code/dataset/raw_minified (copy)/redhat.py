__all__=['RedhatServiceProvider']
from kokki.providers.service import ServiceProvider as A
class RedhatServiceProvider(A):
	def enable_runlevel(A,runlevel):0