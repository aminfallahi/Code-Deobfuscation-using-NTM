'\nPage through multiple features and display an attribute table for each\n'
E=print
import fiona as B,gj2ascii as C
E('Render every feature and its attribute table')
with B.open('sample-data/WV.geojson')as A:
	for D in C.paginate(A,properties=list(A.schema['properties'].keys())):E(D)