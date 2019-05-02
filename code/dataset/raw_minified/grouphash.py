from __future__ import absolute_import
from sentry.api.serializers import Serializer as A,register as B
from sentry.models import GroupHash as C
@B(C)
class D(A):
	def serialize(A,obj,attrs,user):return{'id':obj.hash}