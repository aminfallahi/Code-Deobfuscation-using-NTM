import numpy as C
from osgeo import gdal
def A(filenames):
	'Returns a 3D array containing all band data from all files.';A=[]
	for D in filenames:
		B=gdal.Open(D)
		for E in range(1,B.RasterCount+1):A.append(B.GetRasterBand(E).ReadAsArray())
	return C.dstack(A)