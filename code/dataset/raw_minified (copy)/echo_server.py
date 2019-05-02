import sys,monocle as A
from monocle import _o
A.init(sys.argv[1])
from monocle.stack import eventloop as B
from monocle.stack.network import add_service as C,Service as D
@_o
def E(conn):A=(yield conn.readline());(yield conn.write('you said: %s\r\n'%A.strip()))
C(D(E,7050))
B.run()