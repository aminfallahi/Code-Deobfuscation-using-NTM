D='tools'
import os as A,sys as B
E=A.path.abspath(A.path.split(__file__)[0])
C=A.path.abspath(A.path.join(E,A.pardir))
B.path.insert(0,A.path.join(C,D))
B.path.insert(0,A.path.join(C,D,'six'))
B.path.insert(0,A.path.join(C,D,'html5lib'))
B.path.insert(0,A.path.join(C,D,'wptserve'))
B.path.insert(0,A.path.join(C,D,'pywebsocket','src'))
B.path.insert(0,A.path.join(C,D,'py'))
B.path.insert(0,A.path.join(C,D,'pytest'))
B.path.insert(0,A.path.join(C,D,'webdriver'))