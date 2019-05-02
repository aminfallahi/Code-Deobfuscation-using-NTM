class A:
	'route decorator from https://github.com/peterbe/tornado-utils';_routes=[]
	def __init__(A,regexp):A._regexp=regexp
	def __call__(A,handler):'gets called when we class decorate';B=handler;A._routes.append((A._regexp,B));return B
	@classmethod
	def get_routes(A):return A._routes