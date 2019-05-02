import graphene as A
class B(A.ObjectType):
	hello=A.String();ping=A.String(to=A.String())
	def resolve_hello(A,args,info):return'World'
	def resolve_ping(A,args,info):return 'Pinging {}'.format(args.get('to'))
C=A.Schema(query=B)