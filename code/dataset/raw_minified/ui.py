D=' '
import sys as A
class B:
	def __init__(A,upper=None):A.__min=0.0;A.__max=upper+0.0
	def display(B,value):C=(value-B.__min)/(B.__max-B.__min);E=100*C;F=int(round(80*C));A.stdout.write(D*2+'.'*F+' %4.2f%%\r'%E);A.stdout.flush()
	def clear(B):A.stdout.write(D*(2+80+8)+'\r');A.stdout.flush()