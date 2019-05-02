import puremvc.patterns.proxy
class A(puremvc.patterns.proxy.Proxy):
	NAME='ModelTestProxy';ON_REGISTER_CALLED='onRegister Called';ON_REMOVE_CALLED='onRemove Called'
	def __init__(B):puremvc.patterns.proxy.Proxy.__init__(B,A.NAME,object())
	def onRegister(B):B.setData(A.ON_REGISTER_CALLED)
	def onRemove(B):B.setData(A.ON_REMOVE_CALLED)