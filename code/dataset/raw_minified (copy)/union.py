D='B'
import xcffib as A,struct,six
B={}
C={}
class E(A.Union):
	def __init__(C,unpacker):
		B=unpacker
		if isinstance(B,A.Protobj):B=A.MemoryUnpacker(B.pack())
		A.Union.__init__(C,B);C.data8=A.List(B.copy(),D,20);C.data16=A.List(B.copy(),'H',10);C.data32=A.List(B.copy(),'I',5)
	def pack(C):B=six.BytesIO();B.write(A.pack_list(C.data8,D));return B.getvalue()
A._add_ext(key,unionExtension,B,C)