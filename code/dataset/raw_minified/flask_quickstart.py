from flask import Flask
import begin as A
B=Flask(__name__)
@B.route('/')
def C():return'Hello World!'
@A.start(auto_convert=True,env_prefix='WEB_')
@A.logging
def D(host='127.0.0.1',port=8080,debug=False):B.run(host=host,port=port,debug=debug)