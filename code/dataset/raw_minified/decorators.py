from django.test import TestCase as A
class B(A):
	'\n    Tests for view decorators created using\n    ``django.utils.decorators.decorator_from_middleware``.\n    '
	def test_process_view_middleware(A):'\n        Test a middleware that implements process_view.\n        ';A.client.get('/utils/xview/')