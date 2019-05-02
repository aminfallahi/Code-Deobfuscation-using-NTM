from flask import Flask,render_template,send_from_directory,request
import jinja2,json,IPython.html,os
A=os.path.abspath(os.path.dirname(__file__))+'/example-notebooks'
B=Flask(__name__,static_folder=A)
if __name__=='__main__':B.run(debug=True,port=5001)