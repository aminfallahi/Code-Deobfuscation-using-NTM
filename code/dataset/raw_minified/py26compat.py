import unittest as A
try:B=A.skipIf
except AttributeError:
	def B(condition,reason):
		def A(func):
			def A(*A,**B):return
			if condition:return A
			return func
		return A