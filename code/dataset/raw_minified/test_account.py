from .integration_test_case import IntegrationTestCase as A
class B(A):
	def test_create_account(A):assert A.client.create_account()
	def test_create_account_with_currency(A):B='GBP';assert A.client.create_account(B);assert A.client.create_account(currency=B)
	def test_get_accounts(A):assert A.client.get_accounts(username=A.user['username'])