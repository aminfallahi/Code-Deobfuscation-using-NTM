'\nCanadian postal code validation. The structure of the codes is at:\n\nhttp://www.canadapost.ca/tools/pg/manual/pgaddress-e.asp#1380891\n\n'
import re
from django.utils.translation import ugettext_lazy as C
D=re.compile('^(?P<FSA>[ABCEGHJKLMNPRSTVXYZ]\\d[A-Z])\\s*(?P<LDU>\\d[A-Z]\\d)$')
def A(postcode):
	A=postcode;A=A.upper();B=D.match(A)
	if B:return B.group('FSA')+B.group('LDU')
	else:raise ValueError(C('Invalid postal code for Canada'))