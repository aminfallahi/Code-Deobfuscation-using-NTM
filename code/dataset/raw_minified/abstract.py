import abc as A
class B:
	__metaclass__=A.ABCMeta
	@A.abstractmethod
	def encode(cls,value):0
	@A.abstractmethod
	def decode(cls,data):0
	@classmethod
	def repr(A,value):return repr(value)