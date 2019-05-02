A=0
def C(tree,depth):
	B=depth;A=tree
	if A.left_child:C(A.left_child,B+1)
	A.x=D;A.y=B;D+=1
	if A.right_child:C(A.right_child,B+1)