from tooz import coordination as B
A=B.get_coordinator('zake://',b'host-1')
A.start()
C=A.get_lock('foobar')
with C:print('Do something that is distributed')
A.stop()