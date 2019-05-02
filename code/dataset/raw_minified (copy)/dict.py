from django.utils import six
from django.utils.encoding import smart_bytes as B
def A(uni_dict):
	'\n    Converts a dict of unicode keys into a dict of ascii keys.\n\n    Useful for converting a dict to a kwarg-able format.\n    ';A=uni_dict
	if six.PY3:return A
	return{B(C):D for(C,D)in A.items()}