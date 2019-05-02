'\nSimple interactive process used to demonstrate the use of the\nInteractiveConsole widget.\n'
G='Enter value2: '
F='Enter value1: '
E=int
D=input
C=print
import sys
C('running an interactive process')
if sys.version_info[0]==2:A=raw_input(F);B=raw_input(G)
else:A=D(F);B=D(G)
C('Result: %d'%(E(A)+E(B)))