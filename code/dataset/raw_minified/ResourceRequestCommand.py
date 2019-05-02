from .  import BaseCommand as A
from flask import send_from_directory as B
import os
class C(A):
	def process(A,request,filename,db_session):return B(os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+'/static',filename)
def D():return C()