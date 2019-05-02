class C:
	def __init__(A,tree,depth=0):B=depth;A.x=-1;A.y=B;A.tree=tree;A.children=[C(A,B+1)for A in tree]