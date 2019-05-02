from circuits.web import Server as B,Controller as C,Sessions as D
class E(C):
	def index(A,name='World'):
		C='name';B=name
		if C in A.session:B=A.session[C]
		A.session[C]=B;return'Hello %s!'%B
A=B(('0.0.0.0',8000))
D().register(A)
E().register(A)
A.run()