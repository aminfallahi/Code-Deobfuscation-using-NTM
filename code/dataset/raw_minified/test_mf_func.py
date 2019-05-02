A=[]
def B():A.append(1)
def C():
	while A:A.pop()
def D():assert A,"setup didn't run I think"