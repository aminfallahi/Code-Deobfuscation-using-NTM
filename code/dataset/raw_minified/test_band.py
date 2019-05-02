import logging as A,rasterio,rasterio.env
A.basicConfig(level=A.DEBUG)
def B():
	with rasterio.open('tests/data/RGB.byte.tif')as A:B=rasterio.band(A,1);assert B.ds==A;assert B.bidx==1;assert B.dtype in A.dtypes;assert B.shape==A.shape