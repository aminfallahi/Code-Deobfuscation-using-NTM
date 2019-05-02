from circuits.web import Controller as A
from .helpers import urlopen as B
class C(A):
	def index(A):(yield'Hello ');(yield'World!')
def D(webapp):A=B(webapp.server.http.base);C=A.read();assert C==b'Hello World!'