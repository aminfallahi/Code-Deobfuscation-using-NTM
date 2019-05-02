from django.utils.encoding import force_unicode as B
from django.utils.functional import allow_lazy as C
def A(s,num):
	' truncates a string to a number of letters, similar to truncate_words ';C='...';s=B(s);A=int(num)
	if len(s)>A:
		s=s[:A]
		if not s.endswith(C):s+=C
	return s
A=C(A,unicode)