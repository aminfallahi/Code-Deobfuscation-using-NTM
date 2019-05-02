from dataref import RootDataRef as C
import urlparse as D
def A(firebaseUrl):
	'Construct a new Firebase reference from a full Firebase URL.';A=D.urlparse(firebaseUrl);B=C('https://'+A.netloc)
	if A.path=='/'or A.path=='':return B
	else:return B.child(A.path[1:])