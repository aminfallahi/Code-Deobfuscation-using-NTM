from __future__ import print_function
from twisted.internet import reactor as A
from twisted.internet.endpoints import serverFromString as B
from twisted.web import server as C,static as D
B(A,'onion:80').listen(C.Site(D.Data('Hello, world!','text/plain'))).addCallback(print)
A.run()