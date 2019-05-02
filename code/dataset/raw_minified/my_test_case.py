import unittest as A
from flask import Flask
__all__=['MyTestCase']
class MyTestCase(A.TestCase):
	def setup_app(B):A=Flask(__name__);A.config['TESTING']=True;B.app=A;B.client=A.test_client()