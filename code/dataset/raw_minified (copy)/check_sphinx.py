H='.'
G='-d'
F='sphinx-build'
E='html'
D='doctrees'
A=str
import py,subprocess as B
def C(tmpdir):C=tmpdir;I=C.join(D);J=C.join(E);B.check_call([F,'-W','-bhtml',G,A(I),H,A(J)])
def I(tmpdir):C=tmpdir;I=C.join(D);J=C.join(E);B.check_call([F,'-blinkcheck',G,A(I),H,A(J)])