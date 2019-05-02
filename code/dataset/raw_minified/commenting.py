C='admin'
B='role'
from flask_pundit.application_policy import ApplicationPolicy as A
class D(A):
	def get(A):return A.user.get(B)==C
	class Scope(A.Scope):
		def resolve(A):
			if A.user.get(B)==C:return['Hello']
			return['World']