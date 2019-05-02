A=None
from wsmeext.extdirect import datastore as B
class C(B.DataStoreController):
	__dbsession__=A;__datatype__=A
	def read(B,query=A,sort=A,page=A,start=A,limit=A):
		E=limit;D=start;C=B.__dbsession__.query(B.__datatype__.__saclass__);F=C.count()
		if D is not A and E is not A:C=C.slice(D,E)
		return B.__readresulttype__(data=[B.__datatype__(A)for A in C],success=True,total=F)