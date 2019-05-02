from __future__ import absolute_import,unicode_literals
from .  import RequestTokenEndpoint as C,AuthorizationEndpoint as D
from .  import AccessTokenEndpoint as E,ResourceEndpoint as F
class A(C,D,E,F):
	def __init__(A,request_validator):B=request_validator;C.__init__(A,B);D.__init__(A,B);E.__init__(A,B);F.__init__(A,B)