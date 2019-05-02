from werkzeug.wrappers import Request as B,Response as C
from werkzeug.debug import DebuggedApplication as D
@B.application
def A(request):raise ValueError('testing debugger');return C('hello, world!')
A=D(A,evalex=True)
from werkzeug.serving import run_simple as E
E('localhost',4000,A)