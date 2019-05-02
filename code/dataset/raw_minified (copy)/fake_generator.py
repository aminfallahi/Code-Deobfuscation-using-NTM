class A:
	def __init__(A,dataset,method_name):A.dataset=dataset;A.method_name=method_name
	def __iter__(A):return getattr(A.dataset,A.method_name)()