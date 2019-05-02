from testing.embedding.test_basic import EmbeddingTests as A
class B(A):
	def test_thread_local(A):
		D='tlocal-test';B=A.prepare_module('tlocal');A.compile(D,[B],threads=True)
		for E in range(10):C=A.execute(D);assert C=='done\n'