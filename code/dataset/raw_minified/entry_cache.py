'Cache mixins for Zinnia views'
B=None
class C:
	'\n    Mixin implementing cache on ``get_object`` method.\n    ';_cached_object=B
	def get_object(A,queryset=B):
		'\n        Implement cache on ``get_object`` method to\n        avoid repetitive calls, in POST.\n        '
		if A._cached_object is B:A._cached_object=super(C,A).get_object(queryset)
		return A._cached_object