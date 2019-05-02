import queue
from simpletcp.tcpserver import TCPServer as A
def B(ip,queue,data):queue.put(bytes(''.join([chr(A)for A in reversed(data)]),'UTF-8'))
C=A('localhost',5000,B)
C.run()