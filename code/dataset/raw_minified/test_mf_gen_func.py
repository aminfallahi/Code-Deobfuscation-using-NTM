A=[]
def C():A.append(1)
def D():
	while A:A.pop()
def B(_):assert A,"setup didn't run I think"
def E():(yield(B,1))