import gc,time
while 1:
	A=[]
	for B in xrange(10000000):A.append('foo')
	time.sleep(1)