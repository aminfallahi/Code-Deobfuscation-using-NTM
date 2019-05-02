import os,time,sys
A=0
while True:sys.stdout.write('%d:%d\n'%(os.getpid(),A));sys.stdout.flush();time.sleep(0.1);A+=1