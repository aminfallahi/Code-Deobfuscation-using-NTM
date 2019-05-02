class A:
	def test_multiple_instance_error(A):
		try:A.AppClass()
		except RuntimeError:pass
		except Exception as B:raise B
		else:raise AssertionError('Test failed')