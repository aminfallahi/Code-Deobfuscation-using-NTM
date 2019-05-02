class A:
	def __init__(A,callback):A.callback=callback
	def check(B,ip,paramslist,headers):
		A=None
		def C(key,default=A,l=paramslist):
			if l.has_key(key):return l[key][0]
			return default
		return A