from __future__ import absolute_import,division,print_function,unicode_literals
import subprocess as A,time
from six.moves import xrange as B
for C in B(500):
	D=A.Popen(['python','/home/pi/pi3d/demos/Minimal.py'],stdin=A.PIPE,stderr=A.PIPE);time.sleep(7.0);F,G=D.communicate(chr(27))
	with open('/home/pi/pi3d/experiments/minimal_count.txt','w')as E:E.write(str(C))