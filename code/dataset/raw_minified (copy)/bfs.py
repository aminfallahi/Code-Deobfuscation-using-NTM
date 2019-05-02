def A(graph,start):
	'\n    Traverses a graph using Breadth First Search Algorithm.\n    It returns a set of nodes traversed.\n    ';A,B=set(),[start]
	while B:
		C=B.pop(0)
		if C not in A:A.add(C);B.extend(graph[C]-A)
	return A