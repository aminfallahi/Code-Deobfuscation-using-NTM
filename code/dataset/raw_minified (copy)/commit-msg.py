import sys
from action import run
A='commitmsg'
B=sys.argv[1]
C={'commit_file_path':B}
D=run(A,C)
E=all(D)
if not E:sys.exit(1)