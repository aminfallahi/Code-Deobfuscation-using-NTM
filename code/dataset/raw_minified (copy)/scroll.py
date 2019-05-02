from __future__ import print_function
from pick import pick
A='Select:'
B=['foo.bar%s.baz'%A for A in range(1,71)]
C,D=pick(B,A)
print(C,D)