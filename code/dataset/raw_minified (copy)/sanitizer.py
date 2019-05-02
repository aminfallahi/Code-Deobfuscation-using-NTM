import _base as B
from html5lib.sanitizer import HTMLSanitizerMixin as A
class C(B.Filter,A):
	def __iter__(C):
		for A in B.Filter.__iter__(C):
			A=C.sanitize_token(A)
			if A:(yield A)