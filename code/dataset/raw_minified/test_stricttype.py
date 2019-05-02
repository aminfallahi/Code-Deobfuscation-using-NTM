from collections import namedtuple as B
from msgpack import packb,unpackb as C
def A():
	G=True;A=B('T','foo bar')
	def D(o):
		if isinstance(o,A):return dict(o._asdict())
		raise TypeError('Unsupported type %s'%(type(o),))
	E=packb(A(1,42),strict_types=G,use_bin_type=G,default=D);F=C(E,encoding='utf-8');assert F=={'foo':1,'bar':42}