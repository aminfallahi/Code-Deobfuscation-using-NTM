from win32event import CreateMutex as B
from win32api import CloseHandle as C,GetLastError as D
from winerror import ERROR_ALREADY_EXISTS as A
class E:
	def __init__(A):A.mutexname='testmutex_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}';A.mutex=B(None,False,A.mutexname);A.lasterror=D()
	def aleradyrunning(B):return B.lasterror==A
	def __del__(A):
		if A.mutex:C(A.mutex)