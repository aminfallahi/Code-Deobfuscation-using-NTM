A=NotImplementedError
class B:
	'An abstract CredentialValidator, when inherited it must validate self.user credentials\n    agains self.action'
	def __init__(A,action,user):A.action=action;A.user=user
	def updatePDUWithUserDefaults(B,PDU):'Must update PDU.params from User credential defaults whenever a\n        PDU.params item is None';raise A()
	def validate(B):'Must validate requests through Authorizations and ValueFilters credential check';raise A()