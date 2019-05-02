from __future__ import print_function
F=print
import sys as A,os
A.path.append(os.path.join(os.path.dirname(__file__),'..'))
from fsmonitor import FSMonitor as D
if len(A.argv)<2:F('usage: dirwatch.py [DIRS...]');A.exit(1)
C=D()
for E in A.argv[1:]:C.add_dir_watch(E)
while True:
	for B in C.read_events():F('%s %s %s'%(B.action_name,B.watch.path,B.name))