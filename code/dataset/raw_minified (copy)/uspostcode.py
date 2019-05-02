import re
from django.utils.translation import ugettext_lazy as B
C=re.compile('^\\d{5}(?:-\\d{4})?$')
def A(postcode):
	A=postcode
	if C.search(A):return A
	else:raise ValueError(B('Invalid ZIP code'))