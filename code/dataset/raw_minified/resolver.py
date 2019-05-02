from django.core.urlresolvers import RegexURLResolver as A,Resolver404 as B
class C(Exception):0
class D:
	def __init__(B,conf):B.resolver=A('^',conf)
	def resolve(D,update):
		A=update
		try:E=D.resolver.resolve(A.message.text);return E
		except B:raise C('No handler configured for  %s'%A.message.text)