D=float
from django import template as A
B=A.Library()
@B.filter
def C(kbytes):
	'Returns sizes in human-readable units. Input is kbytes';A=kbytes
	try:A=D(A)
	except (TypeError,ValueError,UnicodeDecodeError):return'unknown'
	C=[(' KB',2**10),(' MB',2**20),(' GB',2**30),(' TB',2**40)]
	for (E,B) in C:
		if A>B:continue
		else:return str(round(A/D(B/2**10),1))+E
C.is_safe=True