from .helpers import urlopen as A
def B(environ,start_response):A='200 OK';B=[('Content-type','text/plain')];start_response(A,B);return'Hello World!'
def C(webapp):B=A(webapp.server.http.base);C=B.read();assert C==b'Hello World!'