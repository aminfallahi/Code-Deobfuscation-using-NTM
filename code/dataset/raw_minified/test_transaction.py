from .integration_test_case import IntegrationTestCase as A
class B(A):
	def test_get_transactions(A):assert A.client.get_transactions()
	def test_get_transaction(A):B=A.build_order(immediate=True);A.client.create_order(B);C=A.client.get_transactions();D=C['transactions'][0];assert A.client.get_transaction(D['id'])
	def test_request_transaction_history(A):assert A.client.request_transaction_history()