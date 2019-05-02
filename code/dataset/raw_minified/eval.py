from jasmin.tools.singleton import Singleton as A
class B:
	'A compiled code holder singleton';__metaclass__=A;nodes={}
	def get(A,pyCode):
		'Return a compiled pyCode object or instanciate a new one';C=pyCode;B=C.encode('hex')
		if B not in A.nodes:A.nodes[B]=compile(C,'','exec')
		return A.nodes[B]