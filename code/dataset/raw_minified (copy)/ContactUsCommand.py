from .  import BaseCommand as A
from flask import render_template as B
class C(A):
	def process(A,request,filename,db_session):return B('contactUs.html')
def D():return C()