from flask import Flask
A=Flask('myflask_flaskapp')
@A.route('/')
@A.route('/<path:path>')
def B():return'<h1>Hello, world!</h1>A flask app brought to you by servi.'
if __name__=='__main__':A.run()