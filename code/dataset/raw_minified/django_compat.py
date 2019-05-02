def A(request_or_item):
	'Returns True if the request_or_item is a Django test case, otherwise False';C=None
	try:from django.test import SimpleTestCase as A
	except ImportError:from django.test import TestCase as A
	B=getattr(request_or_item,'cls',C)
	if B is C:return False
	return issubclass(B,A)