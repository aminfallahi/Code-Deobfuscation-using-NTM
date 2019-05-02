from gevent import monkey as A
A.patch_all()
from gevent.pywsgi import WSGIServer as B
from wsgi import application as C
if __name__=='__main__':D=B(('0.0.0.0',8888),C);D.serve_forever()