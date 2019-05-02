C=[0]*maximum_depth_of_tree
def D(tree,depth=0):
	B=depth;A=tree;A.x=C[B];A.y=B;C[B]+=1
	for E in A.children:D(A,E)