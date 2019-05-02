from benchpy import benchmarked as A
@A()
def B(n):
	if n==0 or n==1:return n
	return n*B(n-1)
B(100)
for (C,D) in A.statistics('factorial').items():print('{} for factorial: {} seconds'.format(C,D[1]))