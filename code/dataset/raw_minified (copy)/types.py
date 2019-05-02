B=TypeError
from tiget.plugins import plugins as A
def C(name):
	for C in A.values():
		try:return C.models[name.lower()]
		except KeyError:pass
	raise B
def D(arg):
	try:A,C=arg.split('=',1)
	except ValueError:raise B('"=" not found in "{}"'.format(arg))
	return A,C