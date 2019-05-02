'!flip [alpha,beta,gamma] - flip a coin n times or shuffle a comma separated list'
import random as A,re
def B(lst):A.shuffle(lst);return ', '.join(lst)
def C(msg,server):
	C=msg.get('text','');A=re.findall('!flip( .*)?',C)
	if not A:return
	D=['heads','tails']if not A[0]else A[0].strip().split(',');return B(D)