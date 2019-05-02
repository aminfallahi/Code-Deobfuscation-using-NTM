import logging as A,email
from google.appengine.ext import webapp as B
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler as C
from google.appengine.ext.webapp.util import run_wsgi_app
class D(C):
	def receive(B,mail_message):A.info('Received a message from: '+mail_message.sender)
E=B.WSGIApplication([D.mapping()],debug=True)