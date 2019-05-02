E='properties'
with features_in_tile_layer(8,41,99,'roads')as D:
	A=set()
	for B in D:
		C=frozenset(B[E].items())
		if C in A:raise Exception('Duplicate properties %r in roads layer, but properties should be unique.'%B[E])
		A.add(C)