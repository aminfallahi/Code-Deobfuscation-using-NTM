from tornado.options import define as A,options
import logging as B
def C(*C,**D):
	try:A(*C,**D)
	except Exception as E:B.error(str(E))