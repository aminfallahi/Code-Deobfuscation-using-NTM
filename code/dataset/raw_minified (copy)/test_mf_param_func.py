A=[]
def C():A.append(1)
def D():
	while A:A.pop()
def B(p):assert A,"setup didn't run I think"
B.paramList=1,