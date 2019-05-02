import time as A
from tooz import coordination as C
D=5
B=C.get_coordinator('zake://',b'host-1')
B.start()
E=A.time()
while A.time()-E<D:B.heartbeat();A.sleep(0.1)
B.stop()