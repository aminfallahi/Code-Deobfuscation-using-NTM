from eventlet import patcher
from eventlet.green import thread
from eventlet.green import time
from eventlet import hubs
hubs.get_hub()
patcher.inject('test.test_thread',globals(),('time',time),('thread',thread))
if __name__=='__main__':
	try:test_main()
	except NameError:pass