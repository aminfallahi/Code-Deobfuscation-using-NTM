from clint.arguments import Args
from clint.textui import puts,colored as C
B=Args().grouped
for A in B:
	if A is not'_':puts(C.red('key:%s'%A));print(B[A].all)