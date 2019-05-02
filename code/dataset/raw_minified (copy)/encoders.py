from rest_framework.utils import encoders as B
class A:
	'\n    Enable the `sort_keys` flag by default, which will cause the JSON keys to\n    be sorted by default.  While this is not the default, and JSON objects are\n    not ordered, it makes testing a bit easier.\n    '
	def __init__(C,*D,**B):B['sort_keys']=True;super(A,C).__init__(*D,**B)
class C(A,B.JSONEncoder):0