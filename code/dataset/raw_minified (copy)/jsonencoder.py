import json as B,datetime as C
from time import mktime as D
class A(B.JSONEncoder):
	'\n    json dump encoder class\n    '
	def default(E,obj):
		'\n        convert datetime instance to str datetime\n        ';A=obj
		if isinstance(A,C.datetime):return int(D(A.timetuple()))
		return B.JSONEncoder.default(E,A)