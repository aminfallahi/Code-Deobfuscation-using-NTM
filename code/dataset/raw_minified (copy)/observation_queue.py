'\nobservation queue used by steppers that return observable actions.\n\nPut this in its own module so it can be imported by pmt \nand can also be optionally imported by steppers.\n'
import collections as A,threading
B=False
C=A.deque()