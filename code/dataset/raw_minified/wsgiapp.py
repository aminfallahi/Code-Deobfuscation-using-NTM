from circuits.web import Controller as A
from circuits.web.wsgi import Application as B
class C(A):
	def index(A):return'Hello World!'
D=B()
C().register(D)