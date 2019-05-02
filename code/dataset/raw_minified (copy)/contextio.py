from __future__ import absolute_import
from contextio.lib.v2_0 import V2_0
from contextio.lib.lite import Lite
def A(consumer_key,consumer_secret,**A):
	C=consumer_secret;B=consumer_key
	if A.get('api_version')=='lite':return Lite(B,C,**A)
	else:return V2_0(B,C,**A)