import socket as A
B=A.socket(A.AF_INET,A.SOCK_STREAM)
B.connect(('127.0.0.1',8888))
C=B.recv(100)
print('Received : {0}'.format(repr(C)))
B.close()