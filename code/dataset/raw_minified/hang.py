from flask import Flask
A=Flask(__name__)
@A.route('/')
def B():return'Hello World!'
if __name__=='__main__':A.run(port=8000)