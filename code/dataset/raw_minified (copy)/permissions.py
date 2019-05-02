from rest_framework import permissions as A
class B(A.BasePermission):
	'\n    Object-level permission to only allow owners of an object to edit it.\n    Assumes the model instance has an `owner` attribute.\n    '
	def has_object_permission(C,request,view,obj):
		B=request
		if B.method in A.SAFE_METHODS:return True
		return obj==B.user