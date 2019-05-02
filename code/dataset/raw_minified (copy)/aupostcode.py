import re
from django.utils.translation import ugettext as B
def A(postcode):
	'\n    Validates Australian postal codes.\n    ';A=postcode;A=A.strip()
	if A.isdigit():return A
	else:raise ValueError(B('Invalid Australian postal code'))