from graph import Graph
def A(sequence):
	A=Graph()
	for B in sequence:
		if not A.has_node(B):A.add_node(B)
	return A
def B(graph):
	A=graph
	for B in A.nodes():
		if sum((A.edge_weight((B,C))for C in A.neighbors(B)))==0:A.del_node(B)