C=classmethod
from inflection import underscore as A,pluralize as B
class D:
	@C
	def default_path(cls):A=cls;return'%s/:id'%A.lookup_key()
	@C
	def lookup_key(cls):C=cls;return A(B(C.__name__))