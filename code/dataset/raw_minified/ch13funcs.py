import matplotlib.pyplot as A
from osgeo import ogr
def B(poly,symbol='k-',**B):
	'Plots a polygon using the given symbol.'
	for C in range(poly.GetGeometryCount()):D=poly.GetGeometryRef(C);E,F=zip(*D.GetPoints());A.plot(E,F,symbol,**B)