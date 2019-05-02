from __future__ import print_function
B=print
import fixpath
from colorama import colorama_text as C,Fore as A
def D():
	'automatically reset stdout'
	with C():B(A.GREEN+'text is green');B(A.RESET+'text is back to normal')
	B('text is back to stdout')
if __name__=='__main__':D()