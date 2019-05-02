I='kind'
H='transit'
G=set
D='properties'
assert_no_matching_feature(7,20,48,H,{I:'railway'})
with features_in_tile_layer(7,20,48,H)as E:
	B=G();F=G(['train','subway','light_rail','tram'])
	for A in E:
		if A[D].get(I)in F:
			C=frozenset(A[D].items())
			if C in B:raise Exception('Duplicate properties %r in transit layer, but properties should be unique.'%A[D])
			B.add(C)