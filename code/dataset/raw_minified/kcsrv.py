import logging as A
from app import app,logger as B
C=A.getLogger()
C.setLevel(A.DEBUG)
A.getLogger('sqlalchemy.engine').setLevel(A.INFO)
if __name__=='__main__':B.warn('This is a debugging configuration. Run with the gunicorn script to run in production.');app.run(host='0.0.0.0',debug=True)