"\nThis is a helper function to run ask-alexa-pykit locally to debug etc\nIt is not intended to be used as a full production server since it doesn't have the requisite HTTPS \nsecurity checks implemented.\n\n"
from flask import Flask,request as B
from lambda_function import lambda_handler as C
A=Flask(__name__)
@A.route('/')
def D():A=B.get_json();return C(A)
if __name__=='__main__':A.run()