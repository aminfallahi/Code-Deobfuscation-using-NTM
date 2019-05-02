_B='socket'
_A='urllib2'
from eventlet import patcher
from eventlet.green import socket
from eventlet.green import urllib2
patcher.inject('test.test_urllib2',globals(),(_B,socket),(_A,urllib2))
HandlerTests.test_file=patcher.patch_function(HandlerTests.test_file,(_B,socket))
HandlerTests.test_cookie_redirect=patcher.patch_function(HandlerTests.test_cookie_redirect,(_A,urllib2))
try:OpenerDirectorTests.test_badly_named_methods=patcher.patch_function(OpenerDirectorTests.test_badly_named_methods,(_A,urllib2))
except AttributeError:pass
if __name__=='__main__':test_main()